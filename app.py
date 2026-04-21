from __future__ import annotations

import streamlit as st


def main() -> None:
    try:
        from eastmed_app import main as eastmed_main
    except ModuleNotFoundError as exc:
        st.set_page_config(
            page_title="EastMed Interactive Briefing",
            page_icon="🌍",
            layout="wide",
            initial_sidebar_state="expanded",
        )
        st.title("Deployment Configuration Issue")
        st.error(
            "This deployment expects `eastmed_app.py` and the `eastmed/` package to be present in the GitHub repository."
        )
        st.code(str(exc))
        st.info(
            "If you intended to deploy the presentation, keep the app entrypoint as `app.py` or `eastmed_app.py` and make sure the full repo was pushed."
        )
        return

    eastmed_main()


if __name__ == "__main__":
    main()
