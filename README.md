# GrayZone Lens

GrayZone Lens is a hackathon-ready prototype for turning curated public-source reporting on the South China Sea into an intelligence-style memo with citations, narrative posture analysis, map context, and linked geo-evidence cards.

## What It Does

- Loads a curated packet of public sources on Second Thomas Shoal / Ayungin Shoal
- Runs a six-step agent pipeline:
  - Source Curator Agent
  - Claim Extraction Agent
  - Corroboration Agent
  - Narrative Posture Agent
  - Geo-Evidence Agent
  - Analyst Memo Agent
- Adds a citation guardrail so unsupported text is not shown as a key judgment
- Renders a lightweight Streamlit experience for live demo use

## Demo Modes

GrayZone Lens supports two execution paths:

- `OpenAI live mode`: uses the OpenAI Responses API with structured outputs when `OPENAI_API_KEY` is available
- `Fallback demo mode`: uses curated seed claims and narrative annotations so the app still works without API setup

## Project Layout

- [app.py](/Users/omar/Downloads/Codex-Hackathong/app.py)
- [grayzone/pipeline.py](/Users/omar/Downloads/Codex-Hackathong/grayzone/pipeline.py)
- [grayzone/models.py](/Users/omar/Downloads/Codex-Hackathong/grayzone/models.py)
- [grayzone/data_loader.py](/Users/omar/Downloads/Codex-Hackathong/grayzone/data_loader.py)
- [grayzone/llm.py](/Users/omar/Downloads/Codex-Hackathong/grayzone/llm.py)
- [grayzone/data/case_packets.json](/Users/omar/Downloads/Codex-Hackathong/grayzone/data/case_packets.json)
- [assets/evidence](/Users/omar/Downloads/Codex-Hackathong/assets/evidence)

## Quick Start

1. Create a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Optional: set your API key.

```bash
export OPENAI_API_KEY="your-key"
export OPENAI_MODEL="gpt-4o-mini"
```

4. Run the app.

```bash
streamlit run app.py
```

## EastMed Briefing

The repository now includes a separate Streamlit presentation entrypoint for the EastMed interactive briefing:

- [eastmed_app.py](/Users/omar/Downloads/Codex-Hackathong/eastmed_app.py)
- [eastmed/content.py](/Users/omar/Downloads/Codex-Hackathong/eastmed/content.py)
- [eastmed/ui.py](/Users/omar/Downloads/Codex-Hackathong/eastmed/ui.py)
- [assets/eastmed](/Users/omar/Downloads/Codex-Hackathong/assets/eastmed)

Run it locally with:

```bash
streamlit run eastmed_app.py
```

## Deploy To Streamlit Community Cloud

According to Streamlit's official Community Cloud docs, Community Cloud deploys from a GitHub repository, copies the full repo, and lets you choose the repository, branch, and entrypoint file during app creation. It currently defaults to Python `3.12`, and Streamlit recommends pinning the Streamlit version in `requirements.txt`, which this repo now does.

Deployment steps:

1. Push this project to a GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with GitHub.
3. Click `Create app`.
4. Select your repository and branch.
5. Set the entrypoint file to `eastmed_app.py`.
6. Open `Advanced settings` and keep Python at `3.12` unless you have a specific reason to choose another supported version.
7. Click `Deploy`.

Notes:

- The current GrayZone demo remains available through `app.py`.
- The EastMed presentation is the file you should choose if you want the presentation deployed.
- If you later change `requirements.txt`, Community Cloud will reinstall dependencies automatically on redeploy.

## Demo Guidance

- Use the `Primary Packet` for the strongest story.
- Keep `Use OpenAI live mode` enabled only if the API key is configured and network access is available.
- If you need a guaranteed rehearsal flow, disable live mode and run the curated fallback pipeline.
- The imagery panels included here are analyst-style evidence cards intended for hackathon demo use. Replace them with externally prepared public imagery before final judging if you have time.

## Notes

- The source packet is curated and prepared for demonstration. It is not a live scraper.
- Forum / social items are intentionally used only for narrative posture analysis and not as primary factual anchors.
