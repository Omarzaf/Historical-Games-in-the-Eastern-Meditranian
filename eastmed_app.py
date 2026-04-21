from __future__ import annotations

from html import escape
from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parent
USE_EMBEDDED_FALLBACK = False

try:
    from eastmed import SLIDES
    from eastmed.ui import (
        ensure_state,
        inject_theme,
        render_navigation,
        render_sidebar,
        render_slide,
    )
except ModuleNotFoundError as exc:
    if exc.name not in {"eastmed", "eastmed.content", "eastmed.ui"}:
        raise
    USE_EMBEDDED_FALLBACK = True
    SLIDES = ()


if USE_EMBEDDED_FALLBACK:
    FALLBACK_SLIDES = (
        {
            "id": 1,
            "section": "Opening",
            "title": "The Geopolitics of Transactionalism",
            "subtitle": "How Eastern Mediterranean states leverage great power rivalry to advance their agendas.",
            "accent": "#C09000",
            "key_stat": {
                "label": "Deck Formula",
                "value": "Geography + Outside Option = Leverage",
                "detail": "Five states, one recurring mechanism across eight decades.",
            },
            "blocks": (
                {
                    "heading": "Defining Argument",
                    "bullets": (
                        "Regional agency comes from exploiting gaps in the global power structure.",
                        "Eastern Mediterranean states did not simply benefit from rivalry; they cultivated it.",
                        "The common move is to become indispensable while keeping another patron plausible.",
                    ),
                },
                {
                    "heading": "How To Read The Deck",
                    "bullets": (
                        "Each case moves from foundation to mechanism to outcomes.",
                        "The comparison is about leverage strategy, not raw national size.",
                    ),
                },
            ),
            "metrics": (
                {"label": "Cases", "value": "5", "detail": "Turkey, Egypt, Israel, Greece, Cyprus"},
                {"label": "Window", "value": "1945-2026", "detail": "The bargaining period covered by the presentation"},
                {"label": "Question", "value": "1", "detail": "How do smaller states extract outsized returns?"},
            ),
            "focus_label": "Opening Focus",
            "focus_items": (
                {
                    "key": "question",
                    "label": "Question",
                    "summary": "The briefing asks how states turn great-power rivalry into bargaining power.",
                    "points": (
                        "This is an analytical question about method rather than a descriptive one about events.",
                        "The same logic shows up in bases, canals, mediation roles, and alliance politics.",
                    ),
                },
                {
                    "key": "thesis",
                    "label": "Thesis",
                    "summary": "Leverage is strongest when a state can supply something a great power needs while signaling that a rival could get it instead.",
                    "points": (
                        "Assets can be geographic, diplomatic, institutional, or infrastructural.",
                        "Credibility matters more than formal size.",
                    ),
                },
            ),
            "comparison": None,
            "visual": "eastmed-hero.svg",
            "visual_caption": "Regional overview linking chokepoints, alliance shelters, and outside options.",
        },
        {
            "id": 2,
            "section": "Turkey",
            "title": "Historical Foundation: 1945-2010",
            "subtitle": "From NATO's southern anchor to a self-described central power.",
            "accent": "#C0392B",
            "key_stat": {
                "label": "Turning Point",
                "value": "1964 Johnson Letter",
                "detail": "The moment Ankara internalized the gap between alliance and national interests.",
            },
            "blocks": (
                {
                    "heading": "Historical Through-Line",
                    "bullets": (
                        "Turkey first monetized vulnerability, then built autonomy, then reframed itself as a gatekeeper.",
                        "Bosphorus control and alliance membership remained central throughout.",
                    ),
                },
            ),
            "metrics": (
                {"label": "1952", "value": "NATO Entry", "detail": "Geography converted into long-term US investment"},
                {"label": "1974", "value": "Cyprus Operation", "detail": "Unilateral action becomes part of the leverage play"},
                {"label": "Montreux", "value": "Chokepoint Control", "detail": "A permanent bargaining asset inside NATO"},
            ),
            "focus_label": "Turkey Historical Phase",
            "focus_items": (
                {
                    "key": "opening",
                    "label": "Opening Move",
                    "summary": "Ankara framed Soviet pressure as a reason Washington had to invest in Turkey.",
                    "points": (
                        "The Truman Doctrine, Marshall aid, and NATO entry flowed from frontier status.",
                        "Incirlik and related facilities turned geography into long-term military relevance.",
                    ),
                },
                {
                    "key": "autonomy",
                    "label": "Autonomy Lesson",
                    "summary": "The Cyprus crises convinced Turkey that leverage required capacity to act without patron permission.",
                    "points": (
                        "The Johnson Letter exposed the limits of dependence on US-provided systems.",
                        "Later Soviet outreach made the outside option more believable.",
                    ),
                },
            ),
            "comparison": None,
            "visual": "turkey-balance.svg",
            "visual_caption": "Turkey's historical logic tied alliance value to strategic geography and unilateral capacity.",
        },
        {
            "id": 3,
            "section": "Turkey",
            "title": "The Mechanism: S-400, NATO Veto, and Triangular Balance",
            "subtitle": "Playing NATO and Russia against each other without fully leaving either camp.",
            "accent": "#C0392B",
            "key_stat": {
                "label": "Mechanism Snapshot",
                "value": "$2.5B S-400 | 18-Month Veto | $7B F-16",
                "detail": "The aim was to make defection look plausible enough to trigger concessions.",
            },
            "blocks": (
                {
                    "heading": "Mechanism Logic",
                    "bullets": (
                        "Turkey used incompatible procurement, veto power, and mediation to raise the price of its cooperation.",
                        "Each move signaled that Ankara could not be treated as a passive alliance consumer.",
                    ),
                },
            ),
            "metrics": (
                {"label": "2019", "value": "S-400 Delivery", "detail": "Maximum signal of strategic independence"},
                {"label": "2022-2024", "value": "Nordic Veto", "detail": "Institutional leverage turned into concessions"},
                {"label": "2024", "value": "$7B F-16", "detail": "Reward timed with Sweden ratification"},
            ),
            "focus_label": "Turkey Lever",
            "focus_items": (
                {
                    "key": "s400",
                    "label": "S-400 Gambit",
                    "summary": "The S-400 was chosen because it was the clearest possible defection signal.",
                    "points": (
                        "A standard NATO-compatible purchase would not have carried the same political meaning.",
                        "The purchase forced allies to reprice Turkish cooperation in other domains.",
                    ),
                },
                {
                    "key": "veto",
                    "label": "NATO Veto",
                    "summary": "Blocking Finland and Sweden turned institutional consent into a tradable asset.",
                    "points": (
                        "Ankara extracted policy shifts before lifting the veto.",
                        "The sequence ending in the F-16 package made the transaction visible.",
                    ),
                },
                {
                    "key": "triangle",
                    "label": "Triangular Balance",
                    "summary": "Turkey used Russia to manage the West and alliance membership to manage Russia.",
                    "points": (
                        "Montreux, mediation, and selective sanctions resistance kept Turkey difficult to isolate.",
                        "The same balance also increased fears that Ankara was overplaying its hand.",
                    ),
                },
            ),
            "comparison": {
                "title": "Turkey's Bargaining Table",
                "left": {
                    "label": "Leverage Used",
                    "value": "Defection Signals",
                    "note": "S-400 purchase, accession veto, Montreux gatekeeping, mediator access",
                },
                "right": {
                    "label": "Return Sought",
                    "value": "Strategic Recognition",
                    "note": "F-16 approval, Black Sea influence, diplomatic centrality, sanction relief",
                },
            },
            "visual": "turkey-balance.svg",
            "visual_caption": "Turkey positioned itself as the pivot between alliance commitments and Russian utility.",
        },
        {
            "id": 4,
            "section": "Turkey",
            "title": "Outcomes: The Cautionary Case of Overreach",
            "subtitle": "Leverage worked until the costs began to outrun the gains.",
            "accent": "#C0392B",
            "key_stat": {
                "label": "Cost-Benefit Ledger",
                "value": "$2.5B Spent, $43B+ Lost Or Blocked",
                "detail": "The S-400 secured tactical concessions but triggered far larger strategic penalties.",
            },
            "blocks": (
                {
                    "heading": "Strategic Lesson",
                    "bullets": (
                        "A credible outside option only works while the primary patron still thinks the relationship is worth preserving.",
                        "Turkey kept leverage tools, but the return on those tools fell sharply.",
                    ),
                },
            ),
            "metrics": (
                {"label": "Gain", "value": "$7B F-16", "detail": "A real concession, but smaller than the strategic losses"},
                {"label": "Loss", "value": "F-35 Exclusion", "detail": "The most expensive cost of the gambit"},
                {"label": "Regional Effect", "value": "Counter-Bloc", "detail": "Greek-Cypriot-Israeli coordination hardened"},
            ),
            "focus_label": "Turkey Outcome Lens",
            "focus_items": (
                {
                    "key": "gains",
                    "label": "Gains",
                    "summary": "Turkey still showed that strategic geography and institutional friction can force major allies to negotiate.",
                    "points": (
                        "The F-16 package and summit language reflected tangible returns.",
                        "Defense-industry growth also showed adaptation under pressure.",
                    ),
                },
                {
                    "key": "costs",
                    "label": "Costs",
                    "summary": "The most important costs were long-term: platform loss, sanctions friction, and coalition response.",
                    "points": (
                        "F-35 exclusion and blocked trade far outweighed the original system cost.",
                        "Turkey's assertiveness helped unify smaller rivals into a more coherent bloc.",
                    ),
                },
            ),
            "comparison": {
                "title": "Outcome Split",
                "left": {
                    "label": "Extracted",
                    "value": "$7B F-16 + Centrality",
                    "note": "Concrete concessions and continued mediator relevance",
                },
                "right": {
                    "label": "Lost",
                    "value": "F-35 + CAATSA + Bloc Formation",
                    "note": "Strategic penalties reshaped the regional environment against Ankara",
                },
            },
            "visual": "turkey-balance.svg",
            "visual_caption": "Turkey kept leverage, but the coalition response raised the price of every future move.",
        },
        {
            "id": 5,
            "section": "Egypt",
            "title": "Historical Foundation: 1945-2010",
            "subtitle": "From non-alignment pioneer to indispensable Arab anchor.",
            "accent": "#1E6B4A",
            "key_stat": {
                "label": "Core Insight",
                "value": "Non-Alignment Is Not Neutrality",
                "detail": "Egypt used outside options to keep every patron bidding for its cooperation.",
            },
            "blocks": (
                {
                    "heading": "Historical Through-Line",
                    "bullets": (
                        "Nasser priced access, Sadat flipped alignment for strategic payoff, and Sisi diversified across patrons.",
                        "The logic stayed consistent even as the international system changed.",
                    ),
                },
            ),
            "metrics": (
                {"label": "1955", "value": "Czech Arms Deal", "detail": "Cairo signals it cannot be cheaply priced"},
                {"label": "1972", "value": "Soviet Expulsion", "detail": "The pivot that opened a US-brokered Sinai return"},
                {"label": "Since 1946", "value": "$85B+ US Aid", "detail": "Long-term reward for becoming a regional anchor"},
            ),
            "focus_label": "Egypt Historical Phase",
            "focus_items": (
                {
                    "key": "nasser",
                    "label": "Nasser",
                    "summary": "Egypt pioneered strategic non-alignment by making both blocs compete for Cairo's alignment.",
                    "points": (
                        "The Czech arms deal and Aswan financing were diplomatic signals as much as procurement decisions.",
                        "Cairo's refusal to be cheaply absorbed forced both superpowers to keep bidding.",
                    ),
                },
                {
                    "key": "sadat",
                    "label": "Sadat",
                    "summary": "Sadat traded a Soviet patron for an American diplomatic payoff: Sinai's return and permanent military financing.",
                    "points": (
                        "The 1973 war was used to create diplomatic conditions rather than a purely battlefield solution.",
                        "Expelling Soviet advisors made Egypt available for realignment on its own terms.",
                    ),
                },
                {
                    "key": "sisi",
                    "label": "Sisi",
                    "summary": "Contemporary Egypt diversified across Washington, Moscow, Beijing, and the Gulf without fully abandoning any of them.",
                    "points": (
                        "Russian arms talks, Chinese investment, and steady US aid all reinforced Egypt's bargaining room.",
                        "The key was to advertise choice rather than to sever the US relationship.",
                    ),
                },
            ),
            "comparison": None,
            "visual": "egypt-corridor.svg",
            "visual_caption": "Egypt's leverage linked Suez transit, Arab diplomacy, and the stability premium.",
        },
        {
            "id": 6,
            "section": "Egypt",
            "title": "The Mechanism: Suez, Mediation, and Niche Diplomacy",
            "subtitle": "Three instruments of leverage operating at the same time.",
            "accent": "#1E6B4A",
            "key_stat": {
                "label": "Mechanism Snapshot",
                "value": "$800M Monthly Canal Losses Became A Bargaining Asset",
                "detail": "Egypt turned vulnerability into compensation by combining transit control with crisis diplomacy.",
            },
            "blocks": (
                {
                    "heading": "Mechanism Logic",
                    "bullets": (
                        "Cairo stacked maritime centrality, Gaza mediation, and migration management into one bargaining position.",
                        "The more outside actors feared Egyptian instability, the more they paid to keep Cairo functional.",
                    ),
                },
            ),
            "metrics": (
                {"label": "Transit", "value": "12-15% Of Global Trade", "detail": "Normal Suez throughput gives Egypt constant relevance"},
                {"label": "Shock", "value": "50% Traffic Collapse", "detail": "The 2024 crisis created urgency for outside support"},
                {"label": "Aid Floor", "value": "$1.3B US FMF", "detail": "Mediation value layered onto an existing military relationship"},
            ),
            "focus_label": "Egypt Lever",
            "focus_items": (
                {
                    "key": "suez",
                    "label": "Suez Canal",
                    "summary": "Suez kept every global power engaged with Cairo because no major maritime actor could ignore it.",
                    "points": (
                        "The canal is both an asset and a vulnerability, which made revenue losses politically legible.",
                        "Egypt could ask for support as compensation for protecting a shared global system.",
                    ),
                },
                {
                    "key": "mediation",
                    "label": "Gaza Mediation",
                    "summary": "Egypt's mediator role made Washington and Arab capitals more willing to relax other points of friction.",
                    "points": (
                        "Cairo became indispensable to ceasefire talks no other regional actor could manage alone.",
                        "That role appeared directly in US aid waivers.",
                    ),
                },
                {
                    "key": "niche",
                    "label": "Niche Diplomacy",
                    "summary": "Egypt concentrated on selected forms of indispensability instead of competing everywhere at once.",
                    "points": (
                        "Migration control, demographic weight, and authoritarian stability all became monetizable services.",
                        "The tactic was to exceed material size in carefully chosen domains.",
                    ),
                },
            ),
            "comparison": {
                "title": "Egypt's Lever Set",
                "left": {
                    "label": "Instrument",
                    "value": "Suez + Mediation + Migration",
                    "note": "Three different channels reinforcing the same bargaining claim",
                },
                "right": {
                    "label": "Return",
                    "value": "Financial And Diplomatic Compensation",
                    "note": "Multilateral support, US waivers, and Arab centrality",
                },
            },
            "visual": "egypt-corridor.svg",
            "visual_caption": "Egypt's leverage worked because canal access, diplomacy, and regional stability were fused together.",
        },
        {
            "id": 7,
            "section": "Egypt",
            "title": "Outcomes: Roughly $60 Billion In A Single Quarter",
            "subtitle": "Monetizing indispensability across Gulf, multilateral, European, and US channels.",
            "accent": "#1E6B4A",
            "key_stat": {
                "label": "Headline Return",
                "value": "~$60B External Support In 2024",
                "detail": "A canal shock and mediation premium became one of the largest rescue packages in the region.",
            },
            "blocks": (
                {
                    "heading": "What Made The Return Distinctive",
                    "bullets": (
                        "Different actors were paying for different parts of Egypt's relevance: stability, canal access, migration management, and crisis mediation.",
                        "The package was not a single negotiation but a layered accumulation of bargains.",
                    ),
                },
            ),
            "metrics": (
                {"label": "Largest Inflow", "value": "$35B UAE", "detail": "Ras El Hikma anchored the financial rescue"},
                {"label": "Multilateral", "value": "$8B IMF", "detail": "Expanded support followed the canal shock"},
                {"label": "European", "value": "EUR8B EU Deal", "detail": "Migration compensation widened the package"},
            ),
            "focus_label": "Egypt Outcome Lens",
            "focus_items": (
                {
                    "key": "package",
                    "label": "Financial Package",
                    "summary": "The 2024 rescue package assembled support from Gulf investors, multilateral lenders, Europe, and Qatar.",
                    "points": (
                        "No single patron carried the whole burden, which made the support more resilient.",
                        "The UAE contribution anchored the package, but other channels widened it dramatically.",
                    ),
                },
                {
                    "key": "waiver",
                    "label": "US Waiver",
                    "summary": "Egypt converted mediation into a US human-rights waiver on the full $1.3B military package.",
                    "points": (
                        "The formal rationale tied the waiver to Egypt's crisis role rather than to internal reform.",
                        "That outcome showed Cairo could transform diplomatic service into hard policy relief.",
                    ),
                },
            ),
            "comparison": {
                "title": "Vulnerability Converted",
                "left": {
                    "label": "Problem",
                    "value": "$7B Revenue Loss",
                    "note": "Suez disruption hit one of Egypt's key income streams",
                },
                "right": {
                    "label": "Return",
                    "value": "8.5x External Support",
                    "note": "Cairo recast the loss as a bargaining case for compensation",
                },
            },
            "visual": "egypt-corridor.svg",
            "visual_caption": "Capital flowed into Egypt from multiple directions because different actors needed different Egyptian services.",
        },
        {
            "id": 8,
            "section": "Israel",
            "title": "Historical Foundation: Cold War To Qualitative Military Edge",
            "subtitle": "From ideological asset to institutionalized strategic partnership.",
            "accent": "#1F6AA5",
            "key_stat": {
                "label": "Institutional Advantage",
                "value": "QME As Doctrine",
                "detail": "Israel turned strategic alignment into a standing entitlement to superior military capability.",
            },
            "blocks": (
                {
                    "heading": "Historical Through-Line",
                    "bullets": (
                        "Israel moved from seeking a guarantor to becoming a strategic force multiplier in US regional policy.",
                        "Military performance and democratic positioning fused into long-term institutional support.",
                    ),
                },
            ),
            "metrics": (
                {"label": "Early Period", "value": "Search For Guarantor", "detail": "Initial survival still depended on external backing"},
                {"label": "1973", "value": "Emergency Airlift", "detail": "Military performance hardened the partnership"},
                {"label": "By 2022", "value": "$150B+ US Aid", "detail": "The cumulative return before the latest crisis surge"},
            ),
            "focus_label": "Israel Historical Phase",
            "focus_items": (
                {
                    "key": "early",
                    "label": "Early Alignment",
                    "summary": "Israel first used ideological positioning to present itself as the reliable democratic partner in a hostile region.",
                    "points": (
                        "The early strategy balanced immigration politics, fragile guarantees, and the search for a durable protector.",
                        "Soviet backing of Arab regimes pushed Israel decisively toward Washington.",
                    ),
                },
                {
                    "key": "performance",
                    "label": "Military Performance",
                    "summary": "Military effectiveness reframed Israel from a sympathetic cause into a strategic asset.",
                    "points": (
                        "The 1967 and 1973 wars made the relationship operational rather than aspirational.",
                        "Emergency resupply strengthened the case for a permanent military edge.",
                    ),
                },
                {
                    "key": "balancing",
                    "label": "Modern Balancing",
                    "summary": "Israel layered US alliance depth with selective Russia coordination and economic engagement with China.",
                    "points": (
                        "Syria deconfliction and Haifa investment showed a more sophisticated multipolar strategy.",
                        "The Abraham Accords moved Israel from periphery to network hub.",
                    ),
                },
            ),
            "comparison": None,
            "visual": "israel-escalation.svg",
            "visual_caption": "Israel's foundational leverage tied ideology, performance, and institutionalized support together.",
        },
        {
            "id": 9,
            "section": "Israel",
            "title": "The Mechanism: Alliance Deepening And Crisis Escalation",
            "subtitle": "Converting a crisis into diplomatic cover, massive resupply, and direct patron entrenchment.",
            "accent": "#1F6AA5",
            "key_stat": {
                "label": "Mechanism Snapshot",
                "value": "6 Vetoes | 78% Arms Share | Direct Iran Strike Support",
                "detail": "The alliance architecture made abstention politically and operationally difficult for Washington.",
            },
            "blocks": (
                {
                    "heading": "Mechanism Logic",
                    "bullets": (
                        "Israel's leverage depends on sustaining an existential framing that makes support appear non-optional.",
                        "Once the alliance moved from sympathy to doctrine, crisis escalation could pull the US deeper.",
                    ),
                },
            ),
            "metrics": (
                {"label": "Support Surge", "value": "800 Planes / 140 Ships", "detail": "Largest military support flow since 1946"},
                {"label": "UNSC Cover", "value": "6 Vetoes", "detail": "Council paralysis became part of the support architecture"},
                {"label": "June 2025", "value": "B-2 Strikes", "detail": "Direct US kinetic action against Iranian nuclear sites"},
            ),
            "focus_label": "Israel Lever",
            "focus_items": (
                {
                    "key": "framing",
                    "label": "Existential Framing",
                    "summary": "The conflict was presented in terms that made restraint look like abandonment rather than policy discretion.",
                    "points": (
                        "That framing activated decades of legal, political, and cultural commitments inside Washington.",
                        "The alliance was already built to move quickly once crisis intensity crossed a threshold.",
                    ),
                },
                {
                    "key": "cover",
                    "label": "Diplomatic Cover",
                    "summary": "Repeated vetoes and procedural shielding reduced international pressure while aid flows expanded.",
                    "points": (
                        "Diplomatic protection reinforced the military relationship rather than sitting beside it.",
                        "The Security Council became functionally weaker on the conflict as US support hardened.",
                    ),
                },
                {
                    "key": "cascade",
                    "label": "Escalation Cascade",
                    "summary": "Regional escalation enlarged the scope of what Washington was already doing for Israel.",
                    "points": (
                        "What began as support for a partner evolved into direct action against that partner's primary regional adversary.",
                        "The mechanism reached its highest activation once the US crossed into direct kinetic participation.",
                    ),
                },
            ),
            "comparison": {
                "title": "Mechanism In Practice",
                "left": {
                    "label": "Institutional Cover",
                    "value": "Doctrine + Veto Power",
                    "note": "QME, legislation, and shielding enabled immediate response",
                },
                "right": {
                    "label": "Escalatory Return",
                    "value": "Deeper US Entrenchment",
                    "note": "Resupply, cover, and kinetic participation expanded together",
                },
            },
            "visual": "israel-escalation.svg",
            "visual_caption": "The mechanism escalated from Gaza to Lebanon, Syria, and Iran while the alliance deepened at each step.",
        },
        {
            "id": 10,
            "section": "Israel",
            "title": "Outcomes: $21.7 Billion And The US As Co-Belligerent",
            "subtitle": "The deepest alliance activation in the set, measured in both money and direct force.",
            "accent": "#1F6AA5",
            "key_stat": {
                "label": "Headline Return",
                "value": "$21.7B Delivered, 751 FMS Cases",
                "detail": "The strategic gain was not only aid volume but the transformation of the patron into an active combat participant.",
            },
            "blocks": (
                {
                    "heading": "Why This Case Is Singular",
                    "bullets": (
                        "Other states extracted financing, access, or modernization. Israel extracted direct patron participation against Iran.",
                        "This is what leverage looks like when alliance doctrine and crisis escalation fully align.",
                    ),
                },
            ),
            "metrics": (
                {"label": "Aid Delivered", "value": "$21.7B", "detail": "Oct. 2023 to Sept. 2025"},
                {"label": "Pipeline", "value": "$39.2B", "detail": "Value of 751 active FMS cases"},
                {"label": "Regional Total", "value": "$31B-$34B", "detail": "Including adjacent regional operations"},
            ),
            "focus_label": "Israel Outcome Lens",
            "focus_items": (
                {
                    "key": "aid",
                    "label": "Aid Scale",
                    "summary": "The two-year surge eclipsed any comparable post-1946 support window in the relationship.",
                    "points": (
                        "Emergency appropriations stacked on top of the standing MOU rather than replacing it.",
                        "The result was both immediate resupply and a deep future pipeline.",
                    ),
                },
                {
                    "key": "activation",
                    "label": "Alliance Activation",
                    "summary": "The most consequential outcome was direct US military participation against Iranian nuclear infrastructure.",
                    "points": (
                        "That crossed a threshold beyond what any other case in the deck extracted.",
                        "It turned the patron from arsenal to operational partner.",
                    ),
                },
            ),
            "comparison": {
                "title": "Alliance Baseline Vs Surge",
                "left": {
                    "label": "Baseline",
                    "value": "$3.8B Annual MOU",
                    "note": "The pre-crisis institutional floor for support",
                },
                "right": {
                    "label": "Crisis Surge",
                    "value": "$17.9B Above Baseline",
                    "note": "Emergency packages accelerated the alliance far beyond its normal annual rhythm",
                },
            },
            "visual": "israel-escalation.svg",
            "visual_caption": "What distinguishes Israel is not just funding scale, but the shift from supplier support to joint military action.",
        },
        {
            "id": 11,
            "section": "Greece + Cyprus",
            "title": "Historical Foundation: Shelter Theory And Operationalized Sovereignty",
            "subtitle": "Two small states solving the same security problem through different institutional tools.",
            "accent": "#7B3FA0",
            "key_stat": {
                "label": "Shared Logic",
                "value": "Internationalize The Local Dispute",
                "detail": "Both states made their security inseparable from something larger powers already cared about.",
            },
            "blocks": (
                {
                    "heading": "Why The Pairing Matters",
                    "bullets": (
                        "Greece used institutions as shelter; Cyprus used crisis and licensing moves to force outside engagement.",
                        "Their leverage became much stronger once they acted as a coordinated bloc rather than as separate small states.",
                    ),
                },
            ),
            "metrics": (
                {"label": "Greece", "value": "Shelter Theory", "detail": "Security bound to NATO and EU commitments"},
                {"label": "Cyprus", "value": "S-300 Crisis", "detail": "Operational sovereignty used to force engagement"},
                {"label": "Post-2010", "value": "Energy Hub Pivot", "detail": "Infrastructure became a new security asset"},
            ),
            "focus_label": "Greece-Cyprus Foundation",
            "focus_items": (
                {
                    "key": "greece",
                    "label": "Greece",
                    "summary": "Greece treated institutional membership as a shield larger partners would be forced to defend.",
                    "points": (
                        "NATO and EU membership made Greek security an institutional concern, not only a national one.",
                        "Later energy infrastructure strengthened the case that Greece was also useful, not just vulnerable.",
                    ),
                },
                {
                    "key": "cyprus",
                    "label": "Cyprus",
                    "summary": "Cyprus used operational moves to drag larger powers into defending its position.",
                    "points": (
                        "The S-300 episode made crisis itself part of the leverage method.",
                        "Licensing Western energy firms in contested waters turned commercial decisions into security obligations.",
                    ),
                },
                {
                    "key": "shared",
                    "label": "Shared Logic",
                    "summary": "Both states solved asymmetry by tying their local disputes to bigger actors' institutional, economic, or legal interests.",
                    "points": (
                        "The weaker the state militarily, the stronger the incentive to internationalize the issue.",
                        "That shared logic set up the later bloc strategy with Israel and the US.",
                    ),
                },
            ),
            "comparison": None,
            "visual": "trilateral-arc.svg",
            "visual_caption": "Greece and Cyprus linked institutional shelter, energy routes, and internationalized security claims.",
        },
        {
            "id": 12,
            "section": "Greece + Cyprus",
            "title": "The Mechanism: Energy Hub, Humanitarian Corridor, And Trilateral Alliance",
            "subtitle": "Collective leverage amplification through logistics, relief access, and bloc formation.",
            "accent": "#7B3FA0",
            "key_stat": {
                "label": "Mechanism Snapshot",
                "value": "Energy Route + Aid Corridor + 3+1 Bloc",
                "detail": "Individually limited states became more valuable once they offered a coherent alternative architecture.",
            },
            "blocks": (
                {
                    "heading": "Mechanism Logic",
                    "bullets": (
                        "Greece handled transit and logistics, Cyprus handled humanitarian access, and the trio together offered Washington a preferred democratic partner bloc.",
                        "The mechanism worked because it bypassed Turkish gatekeeping instead of merely criticizing it.",
                    ),
                },
            ),
            "metrics": (
                {"label": "Greece", "value": "3.1% GDP Defense", "detail": "Reliability reinforced infrastructure value"},
                {"label": "Cyprus", "value": "March 8 2024 Corridor", "detail": "Humanitarian relevance converted into diplomacy"},
                {"label": "Bloc", "value": "Dec. 2025 Joint Plan", "detail": "Security architecture became formal"},
            ),
            "focus_label": "Greece-Cyprus Mechanism",
            "focus_items": (
                {
                    "key": "energy",
                    "label": "Greek Energy Hub",
                    "summary": "Greece made itself strategically useful by offering routes that reduced dependence on Turkish-controlled access points.",
                    "points": (
                        "LNG infrastructure and Alexandroupolis logistics made Athens harder to bypass.",
                        "Reliability, not brinkmanship, was the core of the Greek contribution.",
                    ),
                },
                {
                    "key": "corridor",
                    "label": "Cyprus Corridor",
                    "summary": "Cyprus turned humanitarian positioning into diplomatic capital during the Gaza crisis.",
                    "points": (
                        "Operating the maritime corridor made a small island central to a major emergency.",
                        "That relevance later helped unlock wider institutional gains.",
                    ),
                },
                {
                    "key": "bloc",
                    "label": "Trilateral Bloc",
                    "summary": "The 3+1 framework worked because the three states supplied complementary rather than redundant value.",
                    "points": (
                        "Israel supplied military weight, Greece institutional depth, and Cyprus corridor utility.",
                        "Together they looked like a coherent regional architecture instead of isolated cases.",
                    ),
                },
            ),
            "comparison": {
                "title": "Collective Amplification",
                "left": {
                    "label": "Individually",
                    "value": "Partial Leverage",
                    "note": "Each state had useful assets but limited scale on its own",
                },
                "right": {
                    "label": "Together",
                    "value": "Preferred Partner Bloc",
                    "note": "The trilateral framework created a coherent regional alternative for the US and EU",
                },
            },
            "visual": "trilateral-arc.svg",
            "visual_caption": "The trilateral arc connected Alexandroupolis, Larnaca, and Israeli security capacity into one Western-aligned frame.",
        },
        {
            "id": 13,
            "section": "Greece + Cyprus",
            "title": "Outcomes: $27 Billion Modernization, UNSC Seats, And US Arms Access",
            "subtitle": "Small states, outsized returns once the bloc logic took hold.",
            "accent": "#7B3FA0",
            "key_stat": {
                "label": "Headline Return",
                "value": "$27B Greek Modernization + Cyprus Breakthrough Access",
                "detail": "The bloc produced both hard-security upgrades and institutional elevation.",
            },
            "blocks": (
                {
                    "heading": "Bloc Effect",
                    "bullets": (
                        "Greece alone could not offer a full regional architecture, and Cyprus alone could not justify a US arms-policy shift.",
                        "The alliance multiplied the political meaning of each state's individual gains.",
                    ),
                },
            ),
            "metrics": (
                {"label": "Greece", "value": "$27B Program", "detail": "F-35s, helicopters, frigates, and wider force renewal"},
                {"label": "Cyprus", "value": "167/189 Votes", "detail": "UNHRC margin showed the diplomatic payoff"},
                {"label": "Shared", "value": "UNSC Seats", "detail": "Both states rose together institutionally"},
            ),
            "focus_label": "Greece-Cyprus Outcome Lens",
            "focus_items": (
                {
                    "key": "greece",
                    "label": "Greek Returns",
                    "summary": "Athens translated reliability and route utility into one of the most ambitious modernization programs in modern Greek history.",
                    "points": (
                        "The payoff came through acquisition pipelines, alliance trust, and a new role on NATO's eastern flank.",
                        "Greek leverage looked less dramatic than Turkey's but landed more cleanly.",
                    ),
                },
                {
                    "key": "cyprus",
                    "label": "Cypriot Returns",
                    "summary": "Cyprus moved from frozen-conflict footnote to a state with US arms access and notable UN-level wins.",
                    "points": (
                        "Humanitarian positioning and bloc context made policy change in Washington more plausible.",
                        "The scale of the UN vote showed how much diplomatic ground Nicosia gained.",
                    ),
                },
                {
                    "key": "bloc",
                    "label": "Bloc Effect",
                    "summary": "The whole was greater than the sum of the parts because each partner solved the others' weaknesses.",
                    "points": (
                        "Israel added military heft, Greece institutional depth, and Cyprus added strategic utility in crisis management.",
                        "That combination made the alliance easier for Washington to back openly.",
                    ),
                },
            ),
            "comparison": {
                "title": "Bloc Returns",
                "left": {
                    "label": "Greece",
                    "value": "Defense Capital",
                    "note": "F-35 access, Black Hawks, frigates, and high defense spending",
                },
                "right": {
                    "label": "Cyprus",
                    "value": "Institutional Gains",
                    "note": "Direct US arms access, UN seats, and humanitarian gateway status",
                },
            },
            "visual": "trilateral-arc.svg",
            "visual_caption": "The bloc delivered modernization for Greece and institutional elevation for Cyprus at the same time.",
        },
        {
            "id": 14,
            "section": "Conclusion",
            "title": "What Comes Next: Can Leverage Survive Peace?",
            "subtitle": "Three stress tests for a region where many of the biggest gains were extracted during crisis years.",
            "accent": "#2E75B6",
            "key_stat": {
                "label": "Bottom Line",
                "value": "Agency Is Structural, Not Situational",
                "detail": "The states that endure are the ones that convert temporary crisis value into a lasting asset before the window closes.",
            },
            "blocks": (
                {
                    "heading": "Durability Split",
                    "bullets": (
                        "Greece looks strongest on durability because infrastructure and signed programs outlast the crisis.",
                        "Egypt keeps Suez and the stability premium, but its mediator windfall is harder to repeat.",
                        "Turkey and Israel retain real leverage, but with more fragile political conditions around it.",
                    ),
                },
            ),
            "metrics": (
                {"label": "Stress Tests", "value": "3", "detail": "Gaza framework, Iran trajectory, and durability in stability"},
                {"label": "States", "value": "5", "detail": "Each exits the crisis window with a different asset mix"},
                {"label": "Window", "value": "2023-2026", "detail": "The acute bargaining period covered by the deck"},
            ),
            "focus_label": "Stress Test",
            "focus_items": (
                {
                    "key": "gaza",
                    "label": "Gaza Framework",
                    "summary": "If the ceasefire architecture weakens, states whose leverage depended on mediation and corridor utility lose premium value first.",
                    "points": (
                        "Egypt's mediator premium and Cyprus's corridor relevance are the most exposed.",
                        "Israel also faces a harder politics of alliance management if the framework frays without a clear endpoint.",
                    ),
                },
                {
                    "key": "iran",
                    "label": "Iran Trajectory",
                    "summary": "A decisive shift in Iran changes the strategic logic of multiple cases at once.",
                    "points": (
                        "Israel could lose some of the framing that justified maximum support.",
                        "Turkey could regain value to Washington if regional balancing needs change again.",
                    ),
                },
                {
                    "key": "stability",
                    "label": "Stability Test",
                    "summary": "The biggest question is whether states locked in lasting structures before the crisis premium faded.",
                    "points": (
                        "Greece appears strongest on durability because infrastructure and signed programs outlast the crisis.",
                        "Others kept real assets, but not all of them convert into repeatable leverage under calmer conditions.",
                    ),
                },
            ),
            "comparison": None,
            "visual": "stress-tests.svg",
            "visual_caption": "The regional architecture now depends on whether crisis gains became durable structural assets.",
        },
    )


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
                .stApp {{
                    background:
                        radial-gradient(circle at top left, rgba(192, 144, 0, 0.14), transparent 28%),
                        radial-gradient(circle at top right, rgba(46, 117, 182, 0.16), transparent 26%),
                        linear-gradient(180deg, #f6f8fc 0%, #edf2f9 100%);
                }}
                .block-container {{
                    max-width: 1360px;
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
                .fallback-shell {{
                    background: rgba(255, 255, 255, 0.94);
                    border: 1px solid rgba(22, 45, 78, 0.12);
                    border-radius: 28px;
                    padding: 1.45rem 1.55rem 1.3rem;
                    box-shadow: 0 22px 60px rgba(22, 45, 78, 0.08);
                    backdrop-filter: blur(12px);
                }}
                .fallback-eyebrow {{
                    display: inline-flex;
                    align-items: center;
                    gap: 0.5rem;
                    font-size: 0.78rem;
                    text-transform: uppercase;
                    letter-spacing: 0.12em;
                    font-weight: 700;
                    color: #61718a;
                    margin-bottom: 0.8rem;
                }}
                .fallback-dot {{
                    width: 0.68rem;
                    height: 0.68rem;
                    border-radius: 999px;
                    display: inline-block;
                }}
                .fallback-title {{
                    margin: 0;
                    color: #10233d;
                    font-size: 3rem;
                    line-height: 1.03;
                    letter-spacing: -0.04em;
                    font-weight: 800;
                }}
                .fallback-subtitle {{
                    margin-top: 0.95rem;
                    font-size: 1.08rem;
                    line-height: 1.55;
                    color: #61718a;
                }}
                .fallback-card {{
                    background: rgba(255, 255, 255, 0.95);
                    border: 1px solid rgba(22, 45, 78, 0.12);
                    border-radius: 24px;
                    padding: 1rem 1.05rem;
                    box-shadow: 0 10px 30px rgba(22, 45, 78, 0.05);
                    margin-bottom: 1rem;
                }}
                .fallback-card-title {{
                    margin: 0 0 0.65rem;
                    color: #10233d;
                    font-size: 1.02rem;
                    font-weight: 800;
                }}
                .fallback-card ul {{
                    margin: 0.45rem 0 0 1.05rem;
                    padding: 0;
                    color: #61718a;
                    line-height: 1.55;
                }}
                .fallback-summary {{
                    color: #10233d;
                    line-height: 1.5;
                    margin: 0 0 0.75rem;
                }}
                .fallback-stat {{
                    border-radius: 24px;
                    padding: 1.1rem 1.15rem;
                    color: white;
                }}
                .fallback-stat-label {{
                    font-size: 0.76rem;
                    letter-spacing: 0.12em;
                    text-transform: uppercase;
                    opacity: 0.88;
                    font-weight: 700;
                }}
                .fallback-stat-value {{
                    margin-top: 0.55rem;
                    font-size: 1.58rem;
                    line-height: 1.15;
                    font-weight: 800;
                }}
                .fallback-stat-detail {{
                    margin-top: 0.7rem;
                    font-size: 0.93rem;
                    line-height: 1.45;
                    opacity: 0.92;
                }}
                .fallback-progress-meta {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    gap: 1rem;
                    margin-top: 1rem;
                    color: #61718a;
                    font-size: 0.9rem;
                    font-weight: 600;
                }}
                .fallback-progress-track {{
                    margin-top: 0.55rem;
                    width: 100%;
                    height: 10px;
                    border-radius: 999px;
                    overflow: hidden;
                    background: rgba(16, 35, 61, 0.08);
                }}
                .fallback-progress-fill {{
                    height: 100%;
                    border-radius: 999px;
                }}
                .fallback-metric {{
                    background: rgba(255, 255, 255, 0.96);
                    border: 1px solid rgba(22, 45, 78, 0.12);
                    border-radius: 22px;
                    padding: 0.95rem 1rem;
                    box-shadow: 0 10px 25px rgba(22, 45, 78, 0.05);
                }}
                .fallback-metric-value {{
                    color: #10233d;
                    font-size: 1.24rem;
                    line-height: 1.1;
                    font-weight: 800;
                }}
                .fallback-metric-label {{
                    margin-top: 0.4rem;
                    color: #61718a;
                    font-size: 0.82rem;
                    font-weight: 700;
                    text-transform: uppercase;
                    letter-spacing: 0.08em;
                }}
                .fallback-metric-detail {{
                    margin-top: 0.5rem;
                    color: #61718a;
                    font-size: 0.92rem;
                    line-height: 1.45;
                }}
                .fallback-compare {{
                    background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(245,248,252,0.96));
                    border: 1px solid rgba(22, 45, 78, 0.12);
                    border-radius: 24px;
                    padding: 1rem 1.05rem;
                    box-shadow: 0 10px 30px rgba(22, 45, 78, 0.05);
                    margin-bottom: 1rem;
                }}
                .fallback-compare-grid {{
                    display: grid;
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                    gap: 0.85rem;
                }}
                .fallback-compare-side {{
                    border-radius: 18px;
                    padding: 0.9rem;
                    border: 1px solid rgba(22, 45, 78, 0.12);
                    background: rgba(255, 255, 255, 0.92);
                }}
                .fallback-caption {{
                    margin-top: 0.7rem;
                    color: #61718a;
                    font-size: 0.93rem;
                    line-height: 1.45;
                }}
                @media (max-width: 980px) {{
                    .fallback-title {{
                        font-size: 2.3rem;
                    }}
                    .fallback-compare-grid {{
                        grid-template-columns: 1fr;
                    }}
                }}
            </style>
            """,
            unsafe_allow_html=True,
        )


    def render_sidebar(slides: tuple[dict, ...]) -> None:
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
                format_func=lambda index: f"{slides[index]['id']}. {slides[index]['section']} - {slides[index]['title']}",
            )
            if selected_index != current_index:
                st.session_state.current_slide = selected_index + 1
                st.rerun()

            st.toggle("Presentation mode", key="presentation_mode")
            st.progress(st.session_state.current_slide / len(slides))
            st.caption("Embedded fallback mode is active because the `eastmed/` package was not available in this deployment.")


    def render_navigation(slides: tuple[dict, ...], location: str) -> None:
        current_slide = st.session_state.current_slide
        total = len(slides)
        left, center, next_col, mode_col = st.columns([1.15, 4.0, 1.1, 1.55], gap="small")

        if left.button(
            "Previous",
            disabled=current_slide == 1,
            use_container_width=True,
            key=f"fallback-prev-{location}-{current_slide}",
        ):
            st.session_state.current_slide -= 1
            st.rerun()

        center.markdown(
            f"<div style='margin-top:0.75rem;color:#61718a;font-size:0.92rem;line-height:1.5;'>Screen {current_slide} of {total} · {escape(slides[current_slide - 1]['section'])}</div>",
            unsafe_allow_html=True,
        )

        if next_col.button(
            "Next",
            disabled=current_slide == total,
            use_container_width=True,
            key=f"fallback-next-{location}-{current_slide}",
        ):
            st.session_state.current_slide += 1
            st.rerun()

        toggle_label = "Exit Presentation Mode" if st.session_state.presentation_mode else "Enter Presentation Mode"
        if mode_col.button(toggle_label, use_container_width=True, key=f"fallback-mode-{location}"):
            st.session_state.presentation_mode = not st.session_state.presentation_mode
            st.rerun()


    def render_slide(slide: dict, total_slides: int) -> None:
        accent = slide["accent"]
        progress = int((slide["id"] / total_slides) * 100)
        lead_col, stat_col = st.columns([3.3, 1.35], gap="large")

        with lead_col:
            st.markdown(
                f"""
                <div class="fallback-shell">
                    <div class="fallback-eyebrow">
                        <span class="fallback-dot" style="background:{accent};"></span>
                        <span>{escape(slide["section"])}</span>
                    </div>
                    <h1 class="fallback-title">{escape(slide["title"])}</h1>
                    <p class="fallback-subtitle">{escape(slide["subtitle"])}</p>
                    <div class="fallback-progress-meta">
                        <span>Slide {slide["id"]} / {total_slides}</span>
                        <span>{progress}% through the briefing</span>
                    </div>
                    <div class="fallback-progress-track">
                        <div class="fallback-progress-fill" style="width:{progress}%; background:{accent};"></div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with stat_col:
            stat = slide["key_stat"]
            st.markdown(
                f"""
                <div class="fallback-stat" style="background: linear-gradient(160deg, {accent}, #10233d);">
                    <div class="fallback-stat-label">{escape(stat["label"])}</div>
                    <div class="fallback-stat-value">{escape(stat["value"])}</div>
                    <div class="fallback-stat-detail">{escape(stat["detail"])}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        selected_focus = slide["focus_items"][0]
        if slide["focus_items"]:
            focus_map = {item["key"]: item for item in slide["focus_items"]}
            focus_keys = list(focus_map)
            selected_key = st.radio(
                slide["focus_label"],
                options=focus_keys,
                index=0,
                format_func=lambda key: focus_map[key]["label"],
                horizontal=True,
                key=f"fallback-focus-{slide['id']}",
                label_visibility="collapsed",
            )
            selected_focus = focus_map[selected_key]

        left_col, right_col = st.columns([1.5, 1], gap="large")
        with left_col:
            render_focus_card(selected_focus, accent)
            for block in slide["blocks"]:
                render_block_card(block, accent)

        with right_col:
            render_visual(slide, accent)
            render_comparison(slide["comparison"])

        render_metric_grid(slide["metrics"], accent)


    def render_focus_card(item: dict, accent: str) -> None:
        st.markdown(
            f"""
            <div class="fallback-card" style="border-top: 4px solid {accent};">
                <h3 class="fallback-card-title">{escape(item["label"])}</h3>
                <p class="fallback-summary">{escape(item["summary"])}</p>
                {bullet_list(item["points"])}
            </div>
            """,
            unsafe_allow_html=True,
        )


    def render_block_card(block: dict, accent: str) -> None:
        st.markdown(
            f"""
            <div class="fallback-card" style="border-left: 4px solid {accent};">
                <h3 class="fallback-card-title">{escape(block["heading"])}</h3>
                {bullet_list(block["bullets"])}
            </div>
            """,
            unsafe_allow_html=True,
        )


    def render_visual(slide: dict, accent: str) -> None:
        st.markdown(
            f"""
            <div class="fallback-card" style="border-top: 4px solid {accent}; margin-bottom: 0.6rem;">
                <h3 class="fallback-card-title">Visual Frame</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
        visual_path = ROOT / "assets" / "eastmed" / slide["visual"]
        if visual_path.exists():
            st.image(str(visual_path), use_container_width=True)
        else:
            st.info("Local visual asset not found in this deployment, so the presentation is rendering without the SVG plate.")
        st.markdown(
            f'<div class="fallback-caption">{escape(slide["visual_caption"])}</div>',
            unsafe_allow_html=True,
        )


    def render_metric_grid(metrics: tuple[dict, ...], accent: str) -> None:
        columns = st.columns(len(metrics), gap="small")
        for column, metric in zip(columns, metrics):
            with column:
                st.markdown(
                    f"""
                    <div class="fallback-metric" style="border-top: 4px solid {accent};">
                        <div class="fallback-metric-value">{escape(metric["value"])}</div>
                        <div class="fallback-metric-label">{escape(metric["label"])}</div>
                        <div class="fallback-metric-detail">{escape(metric["detail"])}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


    def render_comparison(comparison: dict | None) -> None:
        if comparison is None:
            return

        st.markdown(
            f"""
            <div class="fallback-compare">
                <h3 class="fallback-card-title">{escape(comparison["title"])}</h3>
                <div class="fallback-compare-grid">
                    <div class="fallback-compare-side">
                        <div class="fallback-metric-label">{escape(comparison["left"]["label"])}</div>
                        <div class="fallback-metric-value">{escape(comparison["left"]["value"])}</div>
                        <div class="fallback-metric-detail">{escape(comparison["left"]["note"])}</div>
                    </div>
                    <div class="fallback-compare-side">
                        <div class="fallback-metric-label">{escape(comparison["right"]["label"])}</div>
                        <div class="fallback-metric-value">{escape(comparison["right"]["value"])}</div>
                        <div class="fallback-metric-detail">{escape(comparison["right"]["note"])}</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


    def bullet_list(items: tuple[str, ...]) -> str:
        rows = "".join(f"<li>{escape(item)}</li>" for item in items)
        return f"<ul>{rows}</ul>"


def main() -> None:
    st.set_page_config(
        page_title="EastMed Interactive Briefing",
        page_icon="🌍",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    slides = FALLBACK_SLIDES if USE_EMBEDDED_FALLBACK else SLIDES
    ensure_state(len(slides))
    inject_theme(st.session_state.presentation_mode)
    render_sidebar(slides)

    render_navigation(slides, location="top")
    st.markdown("")
    render_slide(slides[st.session_state.current_slide - 1], len(slides))
    st.markdown("")
    render_navigation(slides, location="bottom")


if __name__ == "__main__":
    main()
