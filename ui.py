from __future__ import annotations

from html import escape

import streamlit as st

from .content import InteractionItem, SlideBlock, SlideComparison, SlideContent, SlideMetric


def ensure_state(total_slides: int) -> None:
    st.session_state.setdefault("current_slide", 1)
    st.session_state.setdefault("presentation_mode", False)
    if st.session_state.current_slide < 1:
        st.session_state.current_slide = 1
    if st.session_state.current_slide > total_slides:
        st.session_state.current_slide = total_slides


def inject_theme(presentation_mode: bool) -> None:
    sidebar_rules = """
    [data-testid="stSidebar"] { display: none; }
    section[data-testid="stSidebar"] { display: none; }
    """
    if not presentation_mode:
        sidebar_rules = ""

    st.markdown(
        f"""
        <style>
            :root {{
                --navy: #1f3864;
                --steel: #2e75b6;
                --gold: #c09000;
                --light: #eef3f9;
                --card: rgba(255, 255, 255, 0.92);
                --ink: #10233d;
                --muted: #61718a;
                --line: rgba(22, 45, 78, 0.12);
            }}
            .stApp {{
                background:
                    radial-gradient(circle at top left, rgba(192, 144, 0, 0.14), transparent 28%),
                    radial-gradient(circle at top right, rgba(46, 117, 182, 0.16), transparent 26%),
                    linear-gradient(180deg, #f6f8fc 0%, #edf2f9 100%);
            }}
            .block-container {{
                max-width: 1380px;
                padding-top: 1.1rem;
                padding-bottom: 2rem;
            }}
            header[data-testid="stHeader"] {{
                background: transparent;
            }}
            footer {{
                visibility: hidden;
            }}
            div[data-testid="stToolbar"] {{
                visibility: hidden;
                height: 0;
                position: fixed;
            }}
            {sidebar_rules}
            .eastmed-shell {{
                background: var(--card);
                border: 1px solid var(--line);
                border-radius: 28px;
                padding: 1.5rem 1.6rem 1.35rem;
                box-shadow: 0 22px 60px rgba(22, 45, 78, 0.08);
                backdrop-filter: blur(12px);
            }}
            .eastmed-eyebrow {{
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                font-size: 0.78rem;
                text-transform: uppercase;
                letter-spacing: 0.12em;
                font-weight: 700;
                color: var(--muted);
                margin-bottom: 0.8rem;
            }}
            .eastmed-dot {{
                width: 0.68rem;
                height: 0.68rem;
                border-radius: 999px;
                display: inline-block;
            }}
            .eastmed-title {{
                margin: 0;
                color: var(--ink);
                font-size: 3.1rem;
                line-height: 1.02;
                letter-spacing: -0.04em;
                font-weight: 800;
            }}
            .eastmed-subtitle {{
                margin-top: 0.95rem;
                font-size: 1.1rem;
                line-height: 1.55;
                color: var(--muted);
                max-width: 64rem;
            }}
            .eastmed-stat {{
                border-radius: 24px;
                padding: 1.1rem 1.15rem;
                color: white;
                min-height: 100%;
                box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.14);
            }}
            .eastmed-stat-label {{
                font-size: 0.76rem;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                opacity: 0.88;
                font-weight: 700;
            }}
            .eastmed-stat-value {{
                margin-top: 0.55rem;
                font-size: 1.6rem;
                line-height: 1.15;
                font-weight: 800;
            }}
            .eastmed-stat-detail {{
                margin-top: 0.7rem;
                font-size: 0.93rem;
                line-height: 1.45;
                opacity: 0.92;
            }}
            .eastmed-progress-meta {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 1rem;
                margin-top: 1.1rem;
                color: var(--muted);
                font-size: 0.9rem;
                font-weight: 600;
            }}
            .eastmed-progress-track {{
                margin-top: 0.55rem;
                width: 100%;
                height: 10px;
                border-radius: 999px;
                overflow: hidden;
                background: rgba(16, 35, 61, 0.08);
            }}
            .eastmed-progress-fill {{
                height: 100%;
                border-radius: 999px;
            }}
            .eastmed-card {{
                background: rgba(255, 255, 255, 0.94);
                border: 1px solid var(--line);
                border-radius: 24px;
                padding: 1rem 1.05rem;
                box-shadow: 0 10px 30px rgba(22, 45, 78, 0.05);
                margin-bottom: 1rem;
            }}
            .eastmed-card-title {{
                margin: 0 0 0.65rem;
                color: var(--ink);
                font-size: 1.02rem;
                font-weight: 800;
                letter-spacing: -0.01em;
            }}
            .eastmed-card-summary {{
                color: var(--ink);
                line-height: 1.5;
                margin: 0 0 0.75rem;
            }}
            .eastmed-card ul {{
                margin: 0.45rem 0 0 1.05rem;
                padding: 0;
                color: var(--muted);
                line-height: 1.55;
            }}
            .eastmed-metric-card {{
                background: rgba(255, 255, 255, 0.96);
                border: 1px solid var(--line);
                border-radius: 22px;
                padding: 0.95rem 1rem;
                box-shadow: 0 10px 25px rgba(22, 45, 78, 0.05);
                min-height: 100%;
            }}
            .eastmed-metric-value {{
                color: var(--ink);
                font-size: 1.32rem;
                line-height: 1.1;
                font-weight: 800;
                letter-spacing: -0.03em;
            }}
            .eastmed-metric-label {{
                margin-top: 0.4rem;
                color: var(--muted);
                font-size: 0.86rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.08em;
            }}
            .eastmed-metric-detail {{
                margin-top: 0.5rem;
                color: var(--muted);
                font-size: 0.93rem;
                line-height: 1.45;
            }}
            .eastmed-visual-caption {{
                margin-top: 0.7rem;
                color: var(--muted);
                font-size: 0.93rem;
                line-height: 1.45;
            }}
            .eastmed-comparison {{
                background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(245,248,252,0.96));
                border: 1px solid var(--line);
                border-radius: 24px;
                padding: 1rem 1.05rem;
                box-shadow: 0 10px 30px rgba(22, 45, 78, 0.05);
                margin-bottom: 1rem;
            }}
            .eastmed-comparison-title {{
                margin: 0 0 0.85rem;
                color: var(--ink);
                font-size: 1rem;
                font-weight: 800;
            }}
            .eastmed-comparison-grid {{
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 0.85rem;
            }}
            .eastmed-comparison-side {{
                border-radius: 18px;
                padding: 0.9rem;
                border: 1px solid var(--line);
                background: rgba(255, 255, 255, 0.92);
            }}
            .eastmed-comparison-label {{
                text-transform: uppercase;
                font-size: 0.76rem;
                letter-spacing: 0.08em;
                color: var(--muted);
                font-weight: 700;
            }}
            .eastmed-comparison-value {{
                margin-top: 0.35rem;
                font-size: 1.18rem;
                line-height: 1.15;
                font-weight: 800;
                color: var(--ink);
            }}
            .eastmed-comparison-note {{
                margin-top: 0.55rem;
                font-size: 0.92rem;
                line-height: 1.45;
                color: var(--muted);
            }}
            .eastmed-hero-grid {{
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 0.9rem;
            }}
            .eastmed-hero-pill {{
                display: inline-flex;
                align-items: center;
                justify-content: center;
                width: 2rem;
                height: 2rem;
                border-radius: 999px;
                background: rgba(255, 255, 255, 0.16);
                color: white;
                font-weight: 800;
            }}
            .eastmed-inline-note {{
                margin-top: 0.75rem;
                color: var(--muted);
                font-size: 0.92rem;
                line-height: 1.5;
            }}
            .eastmed-sidebar-note {{
                color: var(--muted);
                font-size: 0.92rem;
                line-height: 1.5;
            }}
            @media (max-width: 980px) {{
                .eastmed-title {{
                    font-size: 2.35rem;
                }}
                .eastmed-hero-grid,
                .eastmed-comparison-grid {{
                    grid-template-columns: 1fr;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(slides: tuple[SlideContent, ...]) -> None:
    if st.session_state.presentation_mode:
        return

    current_index = st.session_state.current_slide - 1
    with st.sidebar:
        st.markdown("## EastMed Briefing")
        options = list(range(len(slides)))
        selected_index = st.radio(
            "Jump to screen",
            options=options,
            index=current_index,
            format_func=lambda index: f"{slides[index].id}. {slides[index].section} - {slides[index].title}",
        )
        if selected_index != current_index:
            st.session_state.current_slide = selected_index + 1
            st.rerun()

        st.toggle("Presentation mode", key="presentation_mode")
        st.progress(st.session_state.current_slide / len(slides))
        st.markdown(
            '<p class="eastmed-sidebar-note">This presentation runs as a separate app and does not modify the existing GrayZone workflow.</p>',
            unsafe_allow_html=True,
        )


def render_navigation(slides: tuple[SlideContent, ...], location: str) -> None:
    current_slide = st.session_state.current_slide
    total = len(slides)
    left, center, next_col, mode_col = st.columns([1.15, 4.0, 1.1, 1.55], gap="small")

    if left.button(
        "Previous",
        disabled=current_slide == 1,
        use_container_width=True,
        key=f"eastmed-prev-{location}-{current_slide}",
    ):
        st.session_state.current_slide -= 1
        st.rerun()

    center.markdown(
        f"""
        <div class="eastmed-inline-note">
            Screen {current_slide} of {total} · {escape(slides[current_slide - 1].section)}
        </div>
        """,
        unsafe_allow_html=True,
    )

    toggle_label = "Exit Presentation Mode" if st.session_state.presentation_mode else "Enter Presentation Mode"
    if next_col.button(
        "Next",
        disabled=current_slide == total,
        use_container_width=True,
        key=f"eastmed-next-{location}-{current_slide}",
    ):
        st.session_state.current_slide += 1
        st.rerun()

    if mode_col.button(toggle_label, use_container_width=True, key=f"eastmed-mode-{location}"):
        st.session_state.presentation_mode = not st.session_state.presentation_mode
        st.rerun()


def render_slide(slide: SlideContent, total_slides: int) -> None:
    accent = slide.accent
    lead_col, stat_col = st.columns([3.3, 1.35], gap="large")
    progress = int((slide.id / total_slides) * 100)

    with lead_col:
        st.markdown(
            f"""
            <div class="eastmed-shell">
                <div class="eastmed-eyebrow">
                    <span class="eastmed-dot" style="background:{accent};"></span>
                    <span>{escape(slide.section)}</span>
                </div>
                <h1 class="eastmed-title">{escape(slide.title)}</h1>
                <p class="eastmed-subtitle">{escape(slide.subtitle)}</p>
                <div class="eastmed-progress-meta">
                    <span>Slide {slide.id} / {total_slides}</span>
                    <span>{progress}% through the briefing</span>
                </div>
                <div class="eastmed-progress-track">
                    <div class="eastmed-progress-fill" style="width:{progress}%; background:{accent};"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with stat_col:
        render_key_stat(slide.key_stat, accent)

    if slide.interaction.kind == "hero":
        render_hero_slide(slide)
        return

    selector_key = f"eastmed-selector-{slide.id}"
    option_map = {item.key: item for item in slide.interaction.items}
    option_keys = list(option_map)
    default_index = option_keys.index(slide.interaction.default)
    selected_key = st.radio(
        slide.interaction.label,
        options=option_keys,
        index=default_index,
        format_func=lambda key: option_map[key].label,
        horizontal=True,
        key=selector_key,
        label_visibility="collapsed",
    )
    selected_item = option_map[selected_key]

    if slide.interaction.kind == "stress":
        render_stress_slide(slide, selected_item, accent)
        return

    left_col, right_col = st.columns([1.5, 1], gap="large")
    with left_col:
        render_item_card(selected_item, accent)
        render_supporting_notes(selected_item.supporting, accent)
        render_blocks(slide.blocks, accent)

    with right_col:
        render_visual(slide, accent)
        render_comparison(slide.comparison)

    render_metric_grid(merge_metrics(selected_item.metrics, slide.metrics), accent)


def render_key_stat(metric: SlideMetric, accent: str) -> None:
    st.markdown(
        f"""
        <div class="eastmed-stat" style="background: linear-gradient(160deg, {accent}, #10233d);">
            <div class="eastmed-stat-label">{escape(metric.label)}</div>
            <div class="eastmed-stat-value">{escape(metric.value)}</div>
            <div class="eastmed-stat-detail">{escape(metric.detail)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hero_slide(slide: SlideContent) -> None:
    left_col, right_col = st.columns([1.35, 1], gap="large")
    with left_col:
        render_blocks(slide.blocks, slide.accent)
        hero_cards = []
        for index, item in enumerate(slide.interaction.items, start=1):
            hero_cards.append(
                f"""
                <div class="eastmed-card" style="border-top: 4px solid {slide.accent};">
                    <div class="eastmed-hero-pill">{index}</div>
                    <h3 class="eastmed-card-title" style="margin-top: 0.9rem;">{escape(item.label)}</h3>
                    <p class="eastmed-card-summary">{escape(item.summary)}</p>
                    {bullet_list(item.points)}
                </div>
                """
            )

        st.markdown(
            f'<div class="eastmed-hero-grid">{"".join(hero_cards)}</div>',
            unsafe_allow_html=True,
        )

    with right_col:
        render_visual(slide, slide.accent)
        render_metric_grid(slide.metrics, slide.accent)


def render_item_card(item: InteractionItem, accent: str) -> None:
    st.markdown(
        f"""
        <div class="eastmed-card" style="border-top: 4px solid {accent};">
            <h3 class="eastmed-card-title">{escape(item.label)}</h3>
            <p class="eastmed-card-summary">{escape(item.summary)}</p>
            {bullet_list(item.points)}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_blocks(blocks: tuple[SlideBlock, ...], accent: str) -> None:
    for block in blocks:
        st.markdown(
            f"""
            <div class="eastmed-card" style="border-left: 4px solid {accent};">
                <h3 class="eastmed-card-title">{escape(block.heading)}</h3>
                {bullet_list(block.bullets)}
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_supporting_notes(notes: tuple[str, ...], accent: str) -> None:
    if not notes:
        return

    st.markdown(
        f"""
        <div class="eastmed-card" style="border-left: 4px solid {accent};">
            <h3 class="eastmed-card-title">Additional Signals</h3>
            {bullet_list(notes)}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_visual(slide: SlideContent, accent: str) -> None:
    st.markdown(
        f"""
        <div class="eastmed-card" style="border-top: 4px solid {accent}; margin-bottom: 0.6rem;">
            <h3 class="eastmed-card-title">Visual Frame</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image(str(slide.visual.path), use_container_width=True)
    st.markdown(
        f'<div class="eastmed-visual-caption">{escape(slide.visual.caption)}</div>',
        unsafe_allow_html=True,
    )


def render_metric_grid(metrics: tuple[SlideMetric, ...], accent: str) -> None:
    if not metrics:
        return

    columns = st.columns(len(metrics), gap="small")
    for column, metric in zip(columns, metrics):
        with column:
            st.markdown(
                f"""
                <div class="eastmed-metric-card" style="border-top: 4px solid {accent};">
                    <div class="eastmed-metric-value">{escape(metric.value)}</div>
                    <div class="eastmed-metric-label">{escape(metric.label)}</div>
                    <div class="eastmed-metric-detail">{escape(metric.detail)}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_comparison(comparison: SlideComparison | None) -> None:
    if comparison is None:
        return

    st.markdown(
        f"""
        <div class="eastmed-comparison">
            <h3 class="eastmed-comparison-title">{escape(comparison.title)}</h3>
            <div class="eastmed-comparison-grid">
                <div class="eastmed-comparison-side">
                    <div class="eastmed-comparison-label">{escape(comparison.left.label)}</div>
                    <div class="eastmed-comparison-value">{escape(comparison.left.value)}</div>
                    <div class="eastmed-comparison-note">{escape(comparison.left.note)}</div>
                </div>
                <div class="eastmed-comparison-side">
                    <div class="eastmed-comparison-label">{escape(comparison.right.label)}</div>
                    <div class="eastmed-comparison-value">{escape(comparison.right.value)}</div>
                    <div class="eastmed-comparison-note">{escape(comparison.right.note)}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stress_slide(slide: SlideContent, item: InteractionItem, accent: str) -> None:
    left_col, right_col = st.columns([1.35, 1], gap="large")
    with left_col:
        render_item_card(item, accent)
        render_blocks(slide.blocks, accent)

    with right_col:
        render_visual(slide, accent)
        render_metric_grid(slide.metrics, accent)


def bullet_list(items: tuple[str, ...]) -> str:
    rows = "".join(f"<li>{escape(item)}</li>" for item in items)
    return f"<ul>{rows}</ul>"


def merge_metrics(primary: tuple[SlideMetric, ...], secondary: tuple[SlideMetric, ...]) -> tuple[SlideMetric, ...]:
    if not primary:
        return secondary

    merged = list(primary)
    seen_labels = {metric.label for metric in primary}
    for metric in secondary:
        if metric.label not in seen_labels:
            merged.append(metric)
    return tuple(merged)
