from __future__ import annotations

import os
from pathlib import Path

import pandas as pd
import streamlit as st

from grayzone.data_loader import load_case_packets
from grayzone.pipeline import GrayZonePipeline


ROOT = Path(__file__).resolve().parent


def render_header() -> None:
    st.set_page_config(
        page_title="GrayZone Lens",
        page_icon="🛰️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("GrayZone Lens")
    st.caption(
        "Narrative-to-Geo intelligence briefing for South China Sea gray-zone activity."
    )


def render_packet_overview(packet: dict) -> None:
    st.subheader("Case Packet")
    col1, col2, col3 = st.columns(3)
    col1.metric("Sources", len(packet["sources"]))
    col2.metric("Evidence Panels", len(packet["geo_evidence"]))
    col3.metric("Topic", "South China Sea")

    st.markdown(f"**Selected packet:** {packet['label']}")
    st.write(packet["description"])

    with st.expander("Show curated source registry", expanded=False):
        source_df = pd.DataFrame(
            [
                {
                    "ID": item["source_id"],
                    "Date": item["date"],
                    "Type": item["source_type"],
                    "Publisher": item["publisher"],
                    "Title": item["title"],
                    "Actor Focus": item["actor_focus"],
                }
                for item in packet["sources"]
            ]
        )
        st.dataframe(source_df, use_container_width=True, hide_index=True)


def render_memo(result: dict) -> None:
    memo = result["memo"]
    st.subheader(memo.title)
    st.markdown("### Executive Summary")
    st.write(memo.executive_summary)

    st.markdown("### Key Judgments")
    for item in memo.key_judgments:
        st.markdown(f"**{item.title}**")
        st.write(item.assessment)
        st.caption(
            f"Confidence: {item.confidence} | Citations: {', '.join(item.citations)}"
        )

    st.markdown("### Confidence Assessment")
    st.write(memo.confidence_assessment)

    st.markdown("### Narrative Posture Snapshot")
    st.write(memo.narrative_posture_snapshot)

    st.markdown("### Corroborated Claims")
    for claim in memo.corroborated_claims:
        st.markdown(f"**{claim.title}**")
        st.write(claim.body)
        st.caption(f"Citations: {', '.join(claim.citations)}")

    st.markdown("### Contradictions and Gaps")
    st.write(memo.contradictions_and_gaps)

    st.markdown("### Scenarios and Indicators to Watch")
    st.write(memo.scenarios_and_indicators)

    st.markdown("### Source Annex")
    annex_rows = [
        {"Source": item.source_id, "Title": item.label, "Analyst Note": item.note}
        for item in memo.source_annex
    ]
    st.dataframe(pd.DataFrame(annex_rows), use_container_width=True, hide_index=True)


def render_citations(result: dict) -> None:
    st.subheader("Citation Drill-Down")
    sources_by_id = {item.source_id: item for item in result["sources"]}

    for cluster in result["clusters"]:
        with st.expander(f"{cluster.title} [{cluster.status}]"):
            st.write(cluster.summary)
            st.caption(
                f"Confidence: {cluster.confidence} | Independent sources: {cluster.independent_source_count}"
            )
            for source_id in cluster.source_ids:
                source = sources_by_id[source_id]
                st.markdown(
                    f"- **{source.source_id}** | {source.publisher} | [{source.title}]({source.url})"
                )
                st.write(source.text_excerpt)


def render_narrative(result: dict) -> None:
    st.subheader("Narrative Posture")
    narrative_df = pd.DataFrame(
        [
            {
                "Source": item.source_id,
                "Posture": item.posture_label,
                "Target Actor": item.target_actor,
                "Risk Frame": item.risk_frame,
                "Notes": item.tone_notes,
            }
            for item in result["narratives"]
        ]
    )
    st.dataframe(narrative_df, use_container_width=True, hide_index=True)


def render_map(result: dict) -> None:
    st.subheader("Geo Context")
    markers = result["map_markers"]
    if not markers:
        st.info("No linked markers were produced for this packet.")
        return

    map_df = pd.DataFrame(
        [
            {
                "lat": marker["lat"],
                "lon": marker["lon"],
                "label": marker["label"],
                "status": marker["status"],
            }
            for marker in markers
        ]
    )
    st.map(map_df.rename(columns={"lon": "lon", "lat": "lat"}))
    st.dataframe(
        map_df.rename(
            columns={
                "lat": "Latitude",
                "lon": "Longitude",
                "label": "Location",
                "status": "Analytic Status",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )


def render_evidence(result: dict) -> None:
    st.subheader("Satellite / Geo-Evidence Cards")
    evidence_cards = result["evidence_cards"]
    if not evidence_cards:
        st.info("No evidence cards were linked to corroborated claims.")
        return

    for card in evidence_cards:
        st.markdown(f"**{card.place_name}**")
        image_path = ROOT / card.image_path
        if image_path.exists():
            st.image(str(image_path), use_container_width=True)
        st.caption(
            f"{card.imagery_type} | Confidence note: {card.confidence_note} | Related claim: {card.related_claim_id}"
        )
        st.write(card.annotation_text)


def main() -> None:
    render_header()
    packets = load_case_packets()
    packet_labels = {packet["label"]: packet for packet in packets}

    with st.sidebar:
        st.header("Control Panel")
        packet_label = st.selectbox("Case packet", list(packet_labels.keys()))
        selected_packet = packet_labels[packet_label]

        api_ready = bool(os.getenv("OPENAI_API_KEY"))
        use_live_mode = st.toggle(
            "Use OpenAI live mode",
            value=api_ready,
            help="Structured outputs via the OpenAI Responses API. Falls back to curated demo mode when disabled.",
        )
        st.caption(
            "Live mode is available" if api_ready else "No API key detected; demo mode is recommended."
        )

        run_clicked = st.button("Generate Memo", type="primary", use_container_width=True)

    render_packet_overview(selected_packet)

    if run_clicked:
        with st.spinner("Running GrayZone Lens multi-agent pipeline..."):
            pipeline = GrayZonePipeline(selected_packet, use_live_mode=use_live_mode)
            st.session_state["grayzone_result"] = pipeline.run()

    result = st.session_state.get("grayzone_result")
    if not result:
        st.info("Choose a packet and click `Generate Memo` to produce the intelligence brief.")
        return

    st.success(
        f"Pipeline complete in {result['run_metadata']['elapsed_seconds']:.1f}s via {result['run_metadata']['mode']}."
    )

    memo_tab, citations_tab, narrative_tab, map_tab, evidence_tab = st.tabs(
        ["Memo", "Citations", "Narrative Posture", "Map", "Satellite Evidence"]
    )

    with memo_tab:
        render_memo(result)
    with citations_tab:
        render_citations(result)
    with narrative_tab:
        render_narrative(result)
    with map_tab:
        render_map(result)
    with evidence_tab:
        render_evidence(result)


if __name__ == "__main__":
    main()
