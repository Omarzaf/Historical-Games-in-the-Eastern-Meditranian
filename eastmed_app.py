from __future__ import annotations

import streamlit as st

from eastmed import SLIDES
from eastmed.ui import ensure_state, inject_theme, render_navigation, render_sidebar, render_slide


def main() -> None:
    st.set_page_config(
        page_title="EastMed Interactive Briefing",
        page_icon="🌍",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    ensure_state(len(SLIDES))
    inject_theme(st.session_state.presentation_mode)
    render_sidebar(SLIDES)

    render_navigation(SLIDES, location="top")
    st.markdown("")
    render_slide(SLIDES[st.session_state.current_slide - 1], len(SLIDES))
    st.markdown("")
    render_navigation(SLIDES, location="bottom")


if __name__ == "__main__":
    main()
