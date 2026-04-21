from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class SlideMetric:
    label: str
    value: str
    detail: str


@dataclass(frozen=True)
class SlideBlock:
    heading: str
    bullets: tuple[str, ...]


@dataclass(frozen=True)
class SlideComparisonSide:
    label: str
    value: str
    note: str


@dataclass(frozen=True)
class SlideComparison:
    title: str
    left: SlideComparisonSide
    right: SlideComparisonSide


@dataclass(frozen=True)
class InteractionItem:
    key: str
    label: str
    summary: str
    points: tuple[str, ...]
    metrics: tuple[SlideMetric, ...] = ()
    supporting: tuple[str, ...] = ()


@dataclass(frozen=True)
class SlideVisual:
    asset_name: str
    caption: str

    @property
    def path(self) -> Path:
        return ROOT / "assets" / "eastmed" / self.asset_name


@dataclass(frozen=True)
class SlideInteraction:
    kind: Literal["hero", "timeline", "levers", "outcomes", "stress"]
    label: str
    default: str
    items: tuple[InteractionItem, ...]


@dataclass(frozen=True)
class SlideContent:
    id: int
    section: str
    title: str
    subtitle: str
    accent: str
    key_stat: SlideMetric
    blocks: tuple[SlideBlock, ...]
    metrics: tuple[SlideMetric, ...]
    comparison: SlideComparison | None
    visual: SlideVisual
    interaction: SlideInteraction


SLIDES: tuple[SlideContent, ...] = (
    SlideContent(
        id=1,
        section="Opening",
        title="The Geopolitics of Transactionalism",
        subtitle="How Eastern Mediterranean states leverage great power rivalry to advance their agendas.",
        accent="#C09000",
        key_stat=SlideMetric(
            label="Deck Formula",
            value="Geography + Outside Option = Leverage",
            detail="Five states, one recurring mechanism across eight decades.",
        ),
        blocks=(
            SlideBlock(
                heading="Defining Argument",
                bullets=(
                    "Regional agency is created by navigating gaps in the global power structure.",
                    "These states did not just benefit from rivalry; they cultivated it as a condition of influence.",
                    "The winning move is to become indispensable and credibly hint a rival could get the asset instead.",
                ),
            ),
            SlideBlock(
                heading="How To Read The Cases",
                bullets=(
                    "Each country block moves from historical foundation to mechanism to outcomes.",
                    "The comparison is about structural leverage, not raw national size.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("Cases", "5", "Turkey, Egypt, Israel, Greece, Cyprus"),
            SlideMetric("Window", "1945-2026", "Eight decades of bargaining behavior"),
            SlideMetric("Question", "1", "How do smaller states extract outsized returns?"),
        ),
        comparison=None,
        visual=SlideVisual(
            asset_name="eastmed-hero.svg",
            caption="Regional overview linking chokepoints, institutions, and outside options.",
        ),
        interaction=SlideInteraction(
            kind="hero",
            label="Opening Focus",
            default="question",
            items=(
                InteractionItem(
                    key="question",
                    label="Question",
                    summary="The briefing asks how Eastern Mediterranean states turn great-power rivalry into bargaining power.",
                    points=(
                        "The analysis is about methods, not just outcomes.",
                        "The same logic appears in military basing, mediation, transit routes, and alliance politics.",
                    ),
                ),
                InteractionItem(
                    key="thesis",
                    label="Thesis",
                    summary="Leverage is strongest when a state can supply something a great power needs while keeping an alternative patron plausible.",
                    points=(
                        "Assets can be geographic, diplomatic, institutional, or infrastructural.",
                        "Credibility matters more than formal size.",
                    ),
                ),
                InteractionItem(
                    key="map",
                    label="Mechanism",
                    summary="Across the deck, the key move is not ownership of the asset alone but the ability to redirect it.",
                    points=(
                        "Bases matter because another patron might gain access.",
                        "Corridors matter because another actor could close, reroute, or protect them instead.",
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=2,
        section="Turkey",
        title="Historical Foundation: 1945-2010",
        subtitle="From NATO's southern anchor to a self-described central power.",
        accent="#C0392B",
        key_stat=SlideMetric(
            label="Turning Point",
            value="1964 Johnson Letter",
            detail="The moment Ankara internalized that alliance interests and national interests could diverge.",
        ),
        blocks=(
            SlideBlock(
                heading="Historical Through-Line",
                bullets=(
                    "Turkey first monetized vulnerability, then built autonomy, then reframed itself as a gatekeeper.",
                    "Bosphorus control and alliance membership stayed central through every phase.",
                ),
            ),
            SlideBlock(
                heading="Enduring Lesson",
                bullets=(
                    "Leverage requires a credible ability to act without patron permission.",
                    "Control of a chokepoint inside NATO gave Turkey unusual bargaining room.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("1952", "NATO Membership", "Geography converted into long-term US investment"),
            SlideMetric("1978", "USSR Pact", "Outside option becomes explicit"),
            SlideMetric("2000s", "Central Power", "Montreux control folded into a broader autonomy doctrine"),
        ),
        comparison=None,
        visual=SlideVisual(
            asset_name="turkey-balance.svg",
            caption="Turkey's position between NATO, Russia, and Black Sea access shaped every later bargaining move.",
        ),
        interaction=SlideInteraction(
            kind="timeline",
            label="Turkey Historical Phase",
            default="opening_move",
            items=(
                InteractionItem(
                    key="opening_move",
                    label="1945-1960",
                    summary="Ankara framed Soviet pressure as a reason Washington had to invest in Turkey.",
                    points=(
                        "The Truman Doctrine, Marshall aid, and NATO entry all flowed from Turkey's frontier status.",
                        "Incirlik and other facilities turned geography into sustained military relevance.",
                    ),
                    metrics=(
                        SlideMetric("Asset", "Southern Flank", "The alliance could not ignore the Soviet-facing bridge state"),
                    ),
                ),
                InteractionItem(
                    key="shock",
                    label="1960-1980",
                    summary="The Cyprus crisis convinced Turkey that leverage depended on unilateral capacity, not loyal alignment alone.",
                    points=(
                        "The Johnson Letter exposed the limits of dependence on US hardware.",
                        "The 1974 Cyprus operation and the 1978 Soviet friendship agreement made the outside option credible.",
                    ),
                    metrics=(
                        SlideMetric("Lesson", "Autonomy First", "A patron must believe Ankara can move anyway"),
                    ),
                ),
                InteractionItem(
                    key="central_power",
                    label="1990s-2010",
                    summary="Turkey stopped presenting itself as a passive outpost and started acting as a regional gatekeeper.",
                    points=(
                        "Montreux control let Ankara influence Black Sea military access.",
                        "NATO membership remained useful because it amplified the value of independent action.",
                    ),
                    metrics=(
                        SlideMetric("Chokepoint", "Bosphorus", "A unique bargaining chip within the alliance"),
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=3,
        section="Turkey",
        title="The Mechanism: S-400, NATO Veto, and Triangular Balance",
        subtitle="Playing NATO and Russia against each other without fully leaving either camp.",
        accent="#C0392B",
        key_stat=SlideMetric(
            label="Mechanism Snapshot",
            value="$2.5B S-400 | 18-Month Veto | $7B F-16",
            detail="The leverage play was to make defection look believable enough to trigger concessions.",
        ),
        blocks=(
            SlideBlock(
                heading="Mechanism Logic",
                bullets=(
                    "Turkey used incompatible procurement, veto power, and mediation to remind allies it could not be taken for granted.",
                    "Each move was less about defection itself than about pricing Ankara's cooperation higher.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("2019", "S-400 Delivery", "Maximum signal of strategic independence"),
            SlideMetric("2022-2024", "Nordic Veto", "Institutional leverage converted into concessions"),
            SlideMetric("2024", "$7B F-16 Deal", "Immediate reward after Sweden ratification"),
        ),
        comparison=SlideComparison(
            title="Turkey's Bargaining Table",
            left=SlideComparisonSide(
                label="Leverage Used",
                value="Defection Signals",
                note="S-400 purchase, accession veto, Montreux gatekeeping, mediation access",
            ),
            right=SlideComparisonSide(
                label="Return Sought",
                value="Strategic Recognition",
                note="F-16 approval, diplomatic centrality, Black Sea influence, sanction relief",
            ),
        ),
        visual=SlideVisual(
            asset_name="turkey-balance.svg",
            caption="Turkey positioned itself as the pivot between alliance commitments and Russian utility.",
        ),
        interaction=SlideInteraction(
            kind="levers",
            label="Turkey Leverage Instrument",
            default="s400",
            items=(
                InteractionItem(
                    key="s400",
                    label="S-400 Gambit",
                    summary="The S-400 purchase was chosen because it looked like the clearest possible sign of a live outside option.",
                    points=(
                        "A standard NATO-compatible purchase would not have communicated the same bargaining threat.",
                        "The move forced Washington to price the cost of losing Turkish cooperation in more domains than missile defense.",
                    ),
                ),
                InteractionItem(
                    key="veto",
                    label="NATO Veto",
                    summary="Blocking Finland and Sweden turned institutional consent into a tradable asset.",
                    points=(
                        "Turkey extracted counterterror commitments and policy shifts before relenting.",
                        "The timing of the F-16 notification showed the veto was part of a transactional sequence.",
                    ),
                ),
                InteractionItem(
                    key="triangle",
                    label="Triangular Balance",
                    summary="Ankara used Russia to manage the West and alliance membership to manage Russia.",
                    points=(
                        "Montreux control, Ukraine mediation, and selective sanctions resistance made Turkey hard to isolate.",
                        "The same balancing act also increased fears that Ankara was overplaying its hand.",
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=4,
        section="Turkey",
        title="Outcomes: The Cautionary Case of Overreach",
        subtitle="Leverage worked until the costs began to outrun the gains.",
        accent="#C0392B",
        key_stat=SlideMetric(
            label="Cost-Benefit Ledger",
            value="$2.5B Spent, $43B+ Lost Or Blocked",
            detail="The S-400 secured tactical concessions but triggered far larger strategic penalties.",
        ),
        blocks=(
            SlideBlock(
                heading="What Still Landed",
                bullets=(
                    "$7B F-16 approval, 2024 summit language, and defense-industry growth all showed Ankara could still extract returns.",
                    "Turkey also remained diplomatically central in prisoner exchanges, grain diplomacy, and Gaza negotiations.",
                ),
            ),
            SlideBlock(
                heading="Why This Became A Warning Case",
                bullets=(
                    "F-35 exclusion, CAATSA friction, and the Greece-Cyprus-Israel counter-bloc reduced the value of Turkey's strategy.",
                    "The primary alliance became harder to preserve at the same moment the outside option stayed costly.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("2024", "29% Defense Revenue Growth", "Self-reliance accelerated under pressure"),
            SlideMetric("Program Loss", "$23B F-35 Access", "Removed from the most consequential fighter pipeline"),
            SlideMetric("Counter-Coalition", "Greece-Cyprus-Israel", "Turkish assertiveness unified rivals"),
        ),
        comparison=SlideComparison(
            title="Outcome Split",
            left=SlideComparisonSide(
                label="Extracted",
                value="$7B F-16 + Centrality",
                note="Concrete concessions and continuing mediator status",
            ),
            right=SlideComparisonSide(
                label="Lost",
                value="F-35 + CAATSA + Bloc Formation",
                note="The strategic penalties reshaped the regional balance against Ankara",
            ),
        ),
        visual=SlideVisual(
            asset_name="turkey-balance.svg",
            caption="Turkey kept leverage, but the coalition response raised the price of every future move.",
        ),
        interaction=SlideInteraction(
            kind="outcomes",
            label="Turkey Outcome Lens",
            default="gains",
            items=(
                InteractionItem(
                    key="gains",
                    label="Gains",
                    summary="Turkey still proved that institutional friction and strategic geography can force major allies to negotiate.",
                    points=(
                        "The F-16 deal arrived after Sweden ratification rather than before it.",
                        "Defense exports and summit language showed Ankara could still shape alliance agendas.",
                    ),
                ),
                InteractionItem(
                    key="costs",
                    label="Costs",
                    summary="The most expensive outcome was not a sanction package but the long-term erosion of trust and platform access.",
                    points=(
                        "F-35 removal and blocked spare-parts trade outscaled the value of the original purchase.",
                        "The Greek-Cypriot-Israeli alignment hardened as a direct response to Turkish behavior.",
                    ),
                ),
                InteractionItem(
                    key="lesson",
                    label="Strategic Lesson",
                    summary="A credible outside option works only while the primary patron still thinks the relationship is worth saving.",
                    points=(
                        "Once the patron starts pricing containment above accommodation, leverage becomes self-limiting.",
                        "Turkey kept tools, but the return on those tools fell sharply.",
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=5,
        section="Egypt",
        title="Historical Foundation: 1945-2010",
        subtitle="From non-alignment pioneer to indispensable Arab anchor.",
        accent="#1E6B4A",
        key_stat=SlideMetric(
            label="Core Insight",
            value="Non-Alignment Is Not Neutrality",
            detail="Egypt used outside options to keep every patron bidding for its cooperation.",
        ),
        blocks=(
            SlideBlock(
                heading="Historical Through-Line",
                bullets=(
                    "Nasser priced access, Sadat flipped alignment for strategic payoff, and Sisi diversified rather than choosing one patron.",
                    "The logic stayed the same even as the international system changed.",
                ),
            ),
            SlideBlock(
                heading="What Egypt Perfected",
                bullets=(
                    "Egypt repeatedly converted geostrategic indispensability into finance, diplomacy, and military support.",
                    "Unlike Turkey, Cairo rarely needed a theatrical break to signal it had options.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("1955", "Czech Arms Deal", "The opening signal that Cairo would not be priced cheaply"),
            SlideMetric("1972", "Soviet Expulsion", "Sadat's pivot toward a US-brokered Sinai return"),
            SlideMetric("Since 1946", "$85B+ US Aid", "The long-term reward for becoming a regional anchor"),
        ),
        comparison=None,
        visual=SlideVisual(
            asset_name="egypt-corridor.svg",
            caption="Egypt's leverage linked Suez transit, Arab diplomacy, and the stability premium.",
        ),
        interaction=SlideInteraction(
            kind="timeline",
            label="Egypt Historical Phase",
            default="nasser",
            items=(
                InteractionItem(
                    key="nasser",
                    label="Nasser",
                    summary="Egypt pioneered strategic non-alignment by making both blocs compete for Cairo's alignment.",
                    points=(
                        "The Czech arms deal and Aswan financing were diplomatic signals as much as procurement decisions.",
                        "Cairo's refusal to be cheaply absorbed forced both superpowers to keep bidding.",
                    ),
                ),
                InteractionItem(
                    key="sadat",
                    label="Sadat",
                    summary="Sadat traded a Soviet patron for an American diplomatic payoff: Sinai's return and permanent military financing.",
                    points=(
                        "The 1973 war created the conditions for US-brokered diplomacy rather than a purely battlefield victory.",
                        "Expelling Soviet advisors made Egypt available for realignment on its own terms.",
                    ),
                ),
                InteractionItem(
                    key="sisi",
                    label="Sisi",
                    summary="Contemporary Egypt diversified across Washington, Moscow, Beijing, and the Gulf without abandoning any one channel entirely.",
                    points=(
                        "Russian arms talks, Chinese investment, and steady US aid were all part of a broader hedging strategy.",
                        "The key was to advertise choice, not to fully defect from the US relationship.",
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=6,
        section="Egypt",
        title="The Mechanism: Suez, Mediation, and Niche Diplomacy",
        subtitle="Three instruments of leverage operating at the same time.",
        accent="#1E6B4A",
        key_stat=SlideMetric(
            label="Mechanism Snapshot",
            value="$800M Monthly Canal Losses Became A Bargaining Asset",
            detail="Egypt turned vulnerability into compensation by combining transit control with crisis diplomacy.",
        ),
        blocks=(
            SlideBlock(
                heading="Mechanism Logic",
                bullets=(
                    "Cairo stacked maritime centrality, Gaza mediation, and migration management into one composite bargaining position.",
                    "The more external actors feared Egyptian instability, the more they paid to keep Cairo functional.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("Transit", "12-15% Of Global Trade", "Normal Suez throughput gives Egypt baseline leverage"),
            SlideMetric("Crisis Cost", "50% Traffic Collapse", "The 2024 shock created urgency for outside support"),
            SlideMetric("Aid Baseline", "$1.3B Annual US FMF", "Mediation layered on top of an existing military relationship"),
        ),
        comparison=SlideComparison(
            title="Egypt's Lever Set",
            left=SlideComparisonSide(
                label="Instrument",
                value="Suez + Mediation + Migration",
                note="Three separate channels reinforcing the same bargaining claim",
            ),
            right=SlideComparisonSide(
                label="Return",
                value="Financial And Diplomatic Compensation",
                note="Multilateral support, US waivers, and Arab centrality",
            ),
        ),
        visual=SlideVisual(
            asset_name="egypt-corridor.svg",
            caption="Egypt's leverage worked because canal access, diplomacy, and regional stability were fused together.",
        ),
        interaction=SlideInteraction(
            kind="levers",
            label="Egypt Leverage Instrument",
            default="suez",
            items=(
                InteractionItem(
                    key="suez",
                    label="Suez Canal",
                    summary="Suez ensured every global power had a reason to stay engaged with Cairo even when relations were strained elsewhere.",
                    points=(
                        "The canal is both an asset and a vulnerability, which made revenue losses legible as a shared global problem.",
                        "Egypt could ask for support not as charity but as compensation for protecting a system everyone uses.",
                    ),
                ),
                InteractionItem(
                    key="mediation",
                    label="Gaza Mediation",
                    summary="Egypt's mediator role gave Washington and Arab capitals a reason to relax other points of friction.",
                    points=(
                        "Cairo became indispensable to ceasefire talks that no other regional actor could manage alone.",
                        "That role showed up directly in the waiver of US rights conditions on military aid.",
                    ),
                ),
                InteractionItem(
                    key="niche",
                    label="Niche Diplomacy",
                    summary="Egypt concentrated on specialized forms of indispensability rather than pretending it could compete everywhere at once.",
                    points=(
                        "Migration control, demographic weight, and stability all became monetizable political services.",
                        "The tactic was to exceed material size in carefully selected domains.",
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=7,
        section="Egypt",
        title="Outcomes: Roughly $60 Billion In A Single Quarter",
        subtitle="Monetizing indispensability across Gulf, multilateral, European, and US channels.",
        accent="#1E6B4A",
        key_stat=SlideMetric(
            label="Headline Return",
            value="~$60B External Support In 2024",
            detail="A canal shock and mediation premium became one of the largest rescue packages in the region.",
        ),
        blocks=(
            SlideBlock(
                heading="Why The Return Was So Large",
                bullets=(
                    "Different actors were paying for different parts of Egypt's relevance: stability, canal access, migration management, and crisis mediation.",
                    "The support package was not a single negotiation but a layered accumulation of bargains.",
                ),
            ),
            SlideBlock(
                heading="What Made It Distinctive",
                bullets=(
                    "Egypt extracted aid without making a dramatic break from Washington or paying Turkey-style military costs.",
                    "The model was elegant because it converted shared fear of instability into liquid support.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("Largest Inflow", "$35B UAE", "Ras El Hikma anchored the financial rescue"),
            SlideMetric("Multilateral", "$8B IMF", "Expanded loan package followed the canal shock"),
            SlideMetric("European", "EUR8B EU Deal", "Migration compensation reinforced Cairo's value to Europe"),
        ),
        comparison=SlideComparison(
            title="Vulnerability Converted",
            left=SlideComparisonSide(
                label="Problem",
                value="$7B Revenue Loss",
                note="Suez disruption hit one of Egypt's key income streams",
            ),
            right=SlideComparisonSide(
                label="Return",
                value="8.5x External Support",
                note="Cairo recast the loss as a bargaining case for compensation",
            ),
        ),
        visual=SlideVisual(
            asset_name="egypt-corridor.svg",
            caption="Capital flowed into Egypt from multiple directions because different actors needed different Egyptian services.",
        ),
        interaction=SlideInteraction(
            kind="outcomes",
            label="Egypt Outcome Lens",
            default="package",
            items=(
                InteractionItem(
                    key="package",
                    label="Financial Package",
                    summary="The 2024 rescue package assembled support from Gulf investors, the IMF, the World Bank, Europe, and Qatar.",
                    points=(
                        "No single patron carried the whole burden, which made the support more resilient.",
                        "The UAE contribution anchored the package, but multilateral and European flows widened it dramatically.",
                    ),
                ),
                InteractionItem(
                    key="waiver",
                    label="US Waiver",
                    summary="Egypt converted mediation into a US human-rights waiver on the full $1.3B military package.",
                    points=(
                        "The formal rationale tied the waiver to Egypt's crisis role rather than to internal reform.",
                        "That outcome showed Cairo could transform diplomatic service into hard policy relief.",
                    ),
                ),
                InteractionItem(
                    key="return",
                    label="Analytic Return",
                    summary="Egypt produced the strongest clean leverage-to-return ratio in the presentation without triggering a major coalition backlash.",
                    points=(
                        "The gain was not just scale but efficiency.",
                        "Cairo preserved room with every patron while turning instability into compensation.",
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=8,
        section="Israel",
        title="Historical Foundation: Cold War To Qualitative Military Edge",
        subtitle="From ideological asset to institutionalized strategic partnership.",
        accent="#1F6AA5",
        key_stat=SlideMetric(
            label="Institutional Advantage",
            value="QME As Doctrine",
            detail="Israel turned strategic alignment into a standing entitlement to superior military capability.",
        ),
        blocks=(
            SlideBlock(
                heading="Historical Through-Line",
                bullets=(
                    "Israel moved from seeking a guarantor to becoming a strategic force multiplier in US regional policy.",
                    "Military performance and democratic positioning fused into long-term institutional support.",
                ),
            ),
            SlideBlock(
                heading="Why This Case Is Different",
                bullets=(
                    "Israel is the only case that transformed an ideological narrative into a formalized policy architecture.",
                    "That architecture later made crisis support faster, bigger, and harder to reverse.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("1950s", "Search For Guarantor", "Early survival still depended on external backing"),
            SlideMetric("1973", "Emergency Airlift", "Military performance hardened the partnership"),
            SlideMetric("By 2022", "$150B+ US Aid", "The cumulative return before the latest crisis surge"),
        ),
        comparison=None,
        visual=SlideVisual(
            asset_name="israel-escalation.svg",
            caption="Israel's foundational leverage tied performance, ideology, and institutionalized support together.",
        ),
        interaction=SlideInteraction(
            kind="timeline",
            label="Israel Historical Phase",
            default="early",
            items=(
                InteractionItem(
                    key="early",
                    label="1948-1960s",
                    summary="Israel first used ideological positioning to present itself as the reliable democratic partner in a hostile region.",
                    points=(
                        "The early strategy balanced immigration concerns, fragile guarantees, and the search for a durable protector.",
                        "Soviet backing of Arab regimes pushed Israel decisively toward Washington.",
                    ),
                ),
                InteractionItem(
                    key="performance",
                    label="1967-1973",
                    summary="Military effectiveness reframed Israel from a sympathetic cause into a strategic asset.",
                    points=(
                        "The Six-Day War and Yom Kippur War made the security relationship operational rather than aspirational.",
                        "Emergency resupply strengthened the case for a permanent military edge.",
                    ),
                ),
                InteractionItem(
                    key="balancing",
                    label="2020-Present",
                    summary="Israel layered US alliance depth with selective Russia coordination and economic engagement with China.",
                    points=(
                        "Syria deconfliction and Haifa investment showed a sophisticated multipolar balancing act.",
                        "The Abraham Accords moved Israel from periphery to network hub.",
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=9,
        section="Israel",
        title="The Mechanism: Alliance Deepening And Crisis Escalation",
        subtitle="Converting a crisis into diplomatic cover, massive resupply, and direct patron entrenchment.",
        accent="#1F6AA5",
        key_stat=SlideMetric(
            label="Mechanism Snapshot",
            value="6 Vetoes | 78% Arms Share | Direct Iran Strike Support",
            detail="The institutional alliance architecture made abstention politically and operationally difficult for Washington.",
        ),
        blocks=(
            SlideBlock(
                heading="Mechanism Logic",
                bullets=(
                    "Israel's leverage depends on sustaining an existential framing that makes support appear non-optional.",
                    "Once the alliance moved from sympathy to doctrine, crisis escalation could pull the US deeper in each round.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("Support Surge", "800 Planes / 140 Ships", "Largest military support flow since 1946"),
            SlideMetric("UNSC Cover", "6 Vetoes", "Council paralysis became part of the support architecture"),
            SlideMetric("June 2025", "B-2 Strikes", "Direct US kinetic action against Iranian nuclear sites"),
        ),
        comparison=SlideComparison(
            title="Mechanism In Practice",
            left=SlideComparisonSide(
                label="Institutional Cover",
                value="Doctrine + Veto Power",
                note="QME, legislative support, and diplomatic shielding enabled immediate response",
            ),
            right=SlideComparisonSide(
                label="Escalatory Return",
                value="Deeper US Entrenchment",
                note="Resupply, cover, and kinetic participation expanded together",
            ),
        ),
        visual=SlideVisual(
            asset_name="israel-escalation.svg",
            caption="The mechanism escalated from Gaza to Lebanon, Syria, and Iran while the alliance deepened at each step.",
        ),
        interaction=SlideInteraction(
            kind="levers",
            label="Israel Leverage Instrument",
            default="framing",
            items=(
                InteractionItem(
                    key="framing",
                    label="Existential Framing",
                    summary="The conflict was presented in terms that made restraint look like abandonment rather than policy discretion.",
                    points=(
                        "That framing activated decades of legal, political, and cultural commitments inside Washington.",
                        "The alliance was already built to move quickly once crisis intensity crossed a threshold.",
                    ),
                ),
                InteractionItem(
                    key="cover",
                    label="Diplomatic Cover",
                    summary="Repeated vetoes and procedural shielding reduced international pressure at the same time aid flows expanded.",
                    points=(
                        "Diplomatic protection was not separate from the military relationship; it reinforced it.",
                        "The Security Council became functionally weaker on the conflict as US support hardened.",
                    ),
                ),
                InteractionItem(
                    key="cascade",
                    label="Escalation Cascade",
                    summary="Regional escalation enlarged the scope of what Washington was already doing for Israel.",
                    points=(
                        "What began as support for a partner evolved into direct action against that partner's primary regional adversary.",
                        "The mechanism reached its highest activation once the US crossed into direct kinetic participation.",
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=10,
        section="Israel",
        title="Outcomes: $21.7 Billion And The US As Co-Belligerent",
        subtitle="The deepest alliance activation in the set, measured in both money and direct force.",
        accent="#1F6AA5",
        key_stat=SlideMetric(
            label="Headline Return",
            value="$21.7B Delivered, 751 FMS Cases",
            detail="The strategic gain was not only aid volume but the transformation of the patron into an active combat participant.",
        ),
        blocks=(
            SlideBlock(
                heading="Why This Outcome Is Singular",
                bullets=(
                    "Other states extracted financing, access, or modernization. Israel extracted direct patron participation against Iran.",
                    "The case shows what leverage looks like when alliance doctrine and crisis escalation fully align.",
                ),
            ),
            SlideBlock(
                heading="What The Deck Should Notice",
                bullets=(
                    "This is the most powerful mechanism in the presentation, but also one facing the sharpest long-term scrutiny.",
                    "The same moves that delivered maximum activation may have intensified political limits on future repetition.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("Aid Delivered", "$21.7B", "Oct. 2023 to Sept. 2025"),
            SlideMetric("Pipeline", "$39.2B", "Value of 751 active FMS cases by April 2025"),
            SlideMetric("Regional Total", "$31.35B-$33.77B", "Including Red Sea and Yemen-adjacent support spending"),
        ),
        comparison=SlideComparison(
            title="Alliance Baseline Vs Surge",
            left=SlideComparisonSide(
                label="Baseline",
                value="$3.8B Annual MOU",
                note="The pre-crisis institutional floor for support",
            ),
            right=SlideComparisonSide(
                label="Crisis Surge",
                value="$17.9B Above Baseline",
                note="Emergency packages accelerated the alliance far beyond its normal annual rhythm",
            ),
        ),
        visual=SlideVisual(
            asset_name="israel-escalation.svg",
            caption="What distinguishes Israel is not just funding scale, but the shift from supplier support to joint military action.",
        ),
        interaction=SlideInteraction(
            kind="outcomes",
            label="Israel Outcome Lens",
            default="aid",
            items=(
                InteractionItem(
                    key="aid",
                    label="Aid Scale",
                    summary="The two-year surge eclipsed any comparable post-1946 support window in the relationship.",
                    points=(
                        "Emergency appropriations stacked on top of the standing MOU rather than replacing it.",
                        "The result was both immediate resupply and a deep future pipeline.",
                    ),
                ),
                InteractionItem(
                    key="activation",
                    label="Alliance Activation",
                    summary="The most consequential outcome was direct US military participation against Iranian nuclear infrastructure.",
                    points=(
                        "That crossed a threshold beyond what any other case in the deck extracted.",
                        "It turned the patron from arsenal to operational partner.",
                    ),
                ),
                InteractionItem(
                    key="limits",
                    label="Emerging Limits",
                    summary="Maximum activation may also have intensified international scrutiny and domestic US friction over the durability of unconditional support.",
                    points=(
                        "The mechanism clearly worked in the short run.",
                        "The conclusion asks whether it can keep working at that intensity once the crisis framing changes.",
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=11,
        section="Greece + Cyprus",
        title="Historical Foundation: Shelter Theory And Operationalized Sovereignty",
        subtitle="Two small states solving the same security problem through different institutional tools.",
        accent="#7B3FA0",
        key_stat=SlideMetric(
            label="Shared Logic",
            value="Internationalize The Local Dispute",
            detail="Both states made their security inseparable from something larger powers already cared about.",
        ),
        blocks=(
            SlideBlock(
                heading="What Unites The Cases",
                bullets=(
                    "Greece used institutions as shelter; Cyprus used crisis and licensing moves to force outside engagement.",
                    "Both strategies turned limited military capacity into broader patron responsibility.",
                ),
            ),
            SlideBlock(
                heading="Why The Pairing Matters",
                bullets=(
                    "Their leverage became much stronger once they acted as a coordinated bloc rather than as separate small states.",
                    "The historical logic set up the later trilateral framework with Israel and the US.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("Greece", "Shelter Theory", "Security bound to NATO and EU commitments"),
            SlideMetric("Cyprus", "S-300 Crisis", "Operational sovereignty used to force engagement"),
            SlideMetric("Post-2010", "Energy Hub Pivot", "Infrastructure became a new form of security leverage"),
        ),
        comparison=None,
        visual=SlideVisual(
            asset_name="trilateral-arc.svg",
            caption="Greece and Cyprus linked institutional shelter, energy routes, and internationalized security claims.",
        ),
        interaction=SlideInteraction(
            kind="timeline",
            label="Greece-Cyprus Foundation",
            default="greece",
            items=(
                InteractionItem(
                    key="greece",
                    label="Greece",
                    summary="Greece treated institutional membership as a shield that larger partners would be forced to defend.",
                    points=(
                        "NATO and EU membership made Greek security an institutional concern, not just a national one.",
                        "Later energy infrastructure strengthened the case that Greece was also useful, not only vulnerable.",
                    ),
                ),
                InteractionItem(
                    key="cyprus",
                    label="Cyprus",
                    summary="Cyprus used operational moves to drag larger powers into defending its position.",
                    points=(
                        "The S-300 episode made crisis itself part of the leverage method.",
                        "Licensing Western energy firms in contested waters turned commercial decisions into de facto security commitments.",
                    ),
                ),
                InteractionItem(
                    key="shared",
                    label="Shared Logic",
                    summary="Both states solved asymmetry by tying their local disputes to external actors' institutional, economic, or legal interests.",
                    points=(
                        "The weaker the state militarily, the stronger the incentive to internationalize the issue.",
                        "That shared logic later enabled the bloc strategy with Israel.",
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=12,
        section="Greece + Cyprus",
        title="The Mechanism: Energy Hub, Humanitarian Corridor, And Trilateral Alliance",
        subtitle="Collective leverage amplification through logistics, relief access, and bloc formation.",
        accent="#7B3FA0",
        key_stat=SlideMetric(
            label="Mechanism Snapshot",
            value="Energy Route + Aid Corridor + 3+1 Bloc",
            detail="Individually limited states became much more valuable once they offered a coherent alternative architecture.",
        ),
        blocks=(
            SlideBlock(
                heading="Mechanism Logic",
                bullets=(
                    "Greece handled transit and logistics, Cyprus handled humanitarian access, and the trio together offered Washington a preferred democratic partner bloc.",
                    "The mechanism was strongest because it bypassed Turkish gatekeeping instead of merely complaining about it.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("Greece", "3.1% GDP Defense", "Reliability reinforced infrastructure value"),
            SlideMetric("Cyprus", "March 8 2024 Corridor Launch", "Humanitarian relevance converted into diplomacy"),
            SlideMetric("Bloc", "Dec. 2025 Joint Plan", "Security architecture became formal rather than symbolic"),
        ),
        comparison=SlideComparison(
            title="Collective Amplification",
            left=SlideComparisonSide(
                label="Individually",
                value="Partial Leverage",
                note="Each state had useful assets but limited scale on its own",
            ),
            right=SlideComparisonSide(
                label="Together",
                value="Preferred Partner Bloc",
                note="The trilateral framework created a coherent regional alternative for the US and EU",
            ),
        ),
        visual=SlideVisual(
            asset_name="trilateral-arc.svg",
            caption="The trilateral mechanism connected Alexandroupolis, Larnaca, and Israeli security capacity into one Western-aligned arc.",
        ),
        interaction=SlideInteraction(
            kind="levers",
            label="Greece-Cyprus Mechanism",
            default="energy",
            items=(
                InteractionItem(
                    key="energy",
                    label="Greek Energy Hub",
                    summary="Greece made itself strategically useful by offering Europe and NATO routes that reduced dependence on Turkish-controlled access points.",
                    points=(
                        "LNG infrastructure and Alexandroupolis logistics made Athens harder to bypass.",
                        "Reliability, not brinkmanship, was the core of the Greek contribution.",
                    ),
                ),
                InteractionItem(
                    key="corridor",
                    label="Cyprus Corridor",
                    summary="Cyprus turned humanitarian positioning into diplomatic capital during the Gaza crisis.",
                    points=(
                        "Operating the maritime corridor made a small island central to a major regional emergency.",
                        "That humanitarian relevance later helped unlock broader institutional gains.",
                    ),
                ),
                InteractionItem(
                    key="bloc",
                    label="Trilateral Bloc",
                    summary="The 3+1 framework worked because the three states supplied complementary rather than redundant value.",
                    points=(
                        "Israel supplied military weight, Greece institutional depth, and Cyprus corridor utility.",
                        "Together they looked like a coherent regional architecture rather than three isolated cases.",
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=13,
        section="Greece + Cyprus",
        title="Outcomes: $27 Billion Modernization, UNSC Seats, And US Arms Access",
        subtitle="Small states, outsized returns once the bloc logic took hold.",
        accent="#7B3FA0",
        key_stat=SlideMetric(
            label="Headline Return",
            value="$27B Greek Modernization + Cyprus Breakthrough Access",
            detail="The bloc produced both hard-security upgrades and institutional elevation.",
        ),
        blocks=(
            SlideBlock(
                heading="Why The Bloc Mattered",
                bullets=(
                    "Greece alone could not offer a full regional architecture, and Cyprus alone could not justify a US policy shift on arms access.",
                    "The alliance multiplied the political meaning of each state's individual gains.",
                ),
            ),
            SlideBlock(
                heading="What Stands Out",
                bullets=(
                    "Cyprus converted humanitarian relevance into extraordinary institutional returns for a state of 1.2 million people.",
                    "Greece translated reliability into a modernization program that repositioned it inside NATO's eastern flank.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("Greece", "$27B Program", "F-35s, helicopters, frigates, and wider force renewal"),
            SlideMetric("Cyprus", "167/189 Votes", "UNHRC win underscored the diplomatic payoff"),
            SlideMetric("Shared", "2025-2026 UNSC Seats", "Both states rose together institutionally"),
        ),
        comparison=SlideComparison(
            title="Bloc Returns",
            left=SlideComparisonSide(
                label="Greece",
                value="Defense Capital",
                note="F-35 access, Black Hawks, frigates, and sustained high defense spending",
            ),
            right=SlideComparisonSide(
                label="Cyprus",
                value="Institutional Gains",
                note="Direct US arms access, UN seats, and humanitarian gateway status",
            ),
        ),
        visual=SlideVisual(
            asset_name="trilateral-arc.svg",
            caption="The bloc effect delivered modernization for Greece and institutional elevation for Cyprus at the same time.",
        ),
        interaction=SlideInteraction(
            kind="outcomes",
            label="Greece-Cyprus Outcome Lens",
            default="greece",
            items=(
                InteractionItem(
                    key="greece",
                    label="Greek Returns",
                    summary="Athens translated reliability and route utility into one of the most ambitious modernization programs in modern Greek history.",
                    points=(
                        "The payoff came through acquisition pipelines, alliance trust, and a new role on NATO's eastern flank.",
                        "Greek leverage looked less dramatic than Turkey's but landed more cleanly.",
                    ),
                ),
                InteractionItem(
                    key="cyprus",
                    label="Cypriot Returns",
                    summary="Cyprus moved from frozen-conflict footnote to a state with US arms access and notable UN-level wins.",
                    points=(
                        "Humanitarian positioning and bloc context made policy change in Washington more plausible.",
                        "The scale of the UN vote showed how much diplomatic ground Nicosia gained.",
                    ),
                ),
                InteractionItem(
                    key="bloc",
                    label="Bloc Effect",
                    summary="The whole was greater than the sum of the parts because each partner solved the others' weaknesses.",
                    points=(
                        "Israel added military heft, Greece added institutional depth, and Cyprus added strategic utility in crisis management.",
                        "That combination made the alliance easier for Washington to back openly.",
                    ),
                ),
            ),
        ),
    ),
    SlideContent(
        id=14,
        section="Conclusion",
        title="What Comes Next: Can Leverage Survive Peace?",
        subtitle="Three stress tests for a region where many of the biggest gains were extracted during crisis years.",
        accent="#2E75B6",
        key_stat=SlideMetric(
            label="Bottom Line",
            value="Agency Is Structural, Not Situational",
            detail="The states that endure are the ones that convert temporary crisis value into a lasting asset before the window closes.",
        ),
        blocks=(
            SlideBlock(
                heading="More Durable Assets",
                bullets=(
                    "Greece: Alexandroupolis, LNG routes, and signed modernization programs.",
                    "Egypt: Suez control and the stability premium.",
                    "Cyprus: direct US arms access and current institutional visibility.",
                ),
            ),
            SlideBlock(
                heading="More Crisis-Dependent Assets",
                bullets=(
                    "Turkey: the triangular balance is less rewarding once trust falls and Ukraine conditions shift.",
                    "Egypt: the mediation premium is hard to repeat at 2024 scale.",
                    "Israel: maximum alliance activation may be harder to sustain if the existential framing weakens.",
                ),
            ),
        ),
        metrics=(
            SlideMetric("Stress Tests", "3", "Gaza framework, Iran trajectory, and durability in stability"),
            SlideMetric("States", "5", "Each exits the crisis window with a different asset mix"),
            SlideMetric("Window", "2023-2026", "The acute bargaining period covered by the briefing"),
        ),
        comparison=None,
        visual=SlideVisual(
            asset_name="stress-tests.svg",
            caption="The regional architecture now depends on whether crisis gains have already been converted into durable structural assets.",
        ),
        interaction=SlideInteraction(
            kind="stress",
            label="Stress Test",
            default="gaza",
            items=(
                InteractionItem(
                    key="gaza",
                    label="Gaza Framework",
                    summary="If the ceasefire architecture weakens, the states whose leverage depended on mediation and corridor utility lose premium value first.",
                    points=(
                        "Egypt's mediator premium and Cyprus's corridor relevance are most exposed.",
                        "Israel would also face a harder politics of alliance management if the framework frays without a clear strategic endpoint.",
                    ),
                ),
                InteractionItem(
                    key="iran",
                    label="Iran Trajectory",
                    summary="A decisive shift in Iran changes the strategic logic of multiple cases at once.",
                    points=(
                        "Israel could lose some of the framing that justified maximum support.",
                        "Turkey might regain relative value to Washington if regional balancing needs change again.",
                    ),
                ),
                InteractionItem(
                    key="stability",
                    label="Stability Test",
                    summary="The most important question is whether states built lasting structures before the crisis premium faded.",
                    points=(
                        "Greece appears strongest on durability because infrastructure and signed programs outlast the crisis.",
                        "Others kept real assets, but not all of them convert into repeatable leverage under calmer conditions.",
                    ),
                ),
            ),
        ),
    ),
)
