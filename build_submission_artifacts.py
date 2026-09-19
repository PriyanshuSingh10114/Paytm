import os
import shutil
import pandas as pd
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

base_dir = r"e:\Paytm"

# 1. Generate Executive Summary Markdown
exec_md = """# Paytm Innovation Challenge 2026 — 2-Page Executive Submission

**Track Selected:** Track A — Build Primary-App Preference (Daily Habit & Counter Checkout Shift)  
**Dataset Analyzed:** `Paytm_VOC_Authoritative_Final_Dataset.csv` ($N = 113$ Genuine Responses, $100\%$ Traceable)  
**Annual GMV Opportunity:** ₹5,246 Crore / Year Incremental Run-Rate  

---

## PAGE 1: PROBLEM UNDERSTANDING & VOC EVIDENCE

### 1. The Core Problem
Paytm maintains an extensive active installed base ($63.96\%$ of surveyed respondents have transacted on Paytm UPI in the last 90 days), but suffers from severe **"Moment-of-Checkout Default Loss"** at retail point-of-sale. Paytm captures only $15.32\%$ primary app share, losing $84.68\%$ of high-velocity daily transactions to Google Pay ($45.95\%$) and PhonePe ($30.63\%$) because users reflexively open rival apps at physical counters due to perceived tap-latency, multi-service home screen clutter, and peer network lock-in.

### 2. Target Segment
**High-Velocity Youth, College Students & Young Urban Transactors (Ages 18–26):**
* **$62.16\%$** of the audited dataset are College Students; **$20.72\%$** are Working Professionals.
* **$41.44\%$** execute $\ge 16$ payments weekly ($65\text{--}130+$ monthly transactions), driving maximum counter velocity.
* **$57.45\%$** of non-Paytm primary users in this segment already have active Paytm UPI bank accounts linked.

### 3. Payment Occasions Where the Behavior Occurs
* **Food / Cafés / Canteens:** $54.95\%$ reach (₹30–₹250 AOV; 1–4 daily transactions; high-velocity habit driver).
* **Daily Groceries & Kirana:** $45.05\%$ reach (₹50–₹800 AOV; daily essential retail).
* **Local Shopping & Quick Retail:** $56.76\%$ reach (₹200–₹2,500 AOV; major offline GMV anchor).
* **P2P Peer Transfers & Daily Commute:** $41.44\%$ & $37.84\%$ reach (Social splitting & transit anchors).

### 4. Key Quantified VOC Findings ($N = 113$)
1. **Speed & Habit Dominate App Choice ($77.5\%$ combined):** $45.05\%$ pick their primary app because *"It is faster or easier"* and $32.43\%$ because *"It is simply my habit / default"*. Stated rewards trail far behind at $14.41\%$.
2. **The Dormant-Default Paradox:** $57.45\%$ of Google Pay and PhonePe users ($54/94$) are 90-day active on Paytm UPI.
3. **The Root Barriers:** $36.94\%$ cite *"I automatically use another app"* (muscle memory) and $24.32\%$ cite *"Another app feels faster / easier"* (perceived tap-latency).
4. **Latent Readiness:** $12.61\%$ explicitly stated *"Nothing — I could use Paytm more"*, confirming zero brand refusal.

### 5. Core Behavioral Insight
> *"UPI checkout at merchant counters is a System-1 subconscious reflex governed by cognitive ease and tap-latency. Because Paytm presents a comprehensive financial super-app home screen, users experience micro-hesitation at crowded counters, defaulting to single-purpose rival interfaces. Losing this daily micro-transaction breaks the payment habit, causing Paytm to lose the high-ticket monthly billings and P2P transfers that naturally follow."*

### 6. Quantified Opportunity
* **Addressable Youth Transactors:** $16.56\text{ Million}$ active Paytm-registered youth transactors currently defaulting to rival apps.
* **12-Month Conversion Target ($15\%$ Shift):** $2.484\text{ Million}$ converted Monthly Transacting Users (MTUs).
* **Shift Impact:** $+8$ transactions/month shifted to Paytm default @ ₹$220$ blended offline AOV.
* **Derived Incremental GMV:** **₹437.2 Crore / Month** (**₹5,246 Crore / Year** Annualized Run-Rate).

---

## PAGE 2: PROPOSED SOLUTION & EXECUTION PLAN

### 7. The Solution: Paytm TurboScan & SplitPass
A twin-engine product intervention designed to capture physical counter checkout speed and viral campus peer loops:
1. **Paytm TurboScan (Sub-500ms Lockscreen Scanner):** An OS-level lockscreen/home-widget scanner executing biometric-to-payment in <500ms, completely bypassing the super-app feed for instant counter checkouts.
2. **Paytm SplitPass (Soundbox-Integrated Group Bill Splitting):** A 1-tap group bill splitting tool that triggers instant peer settlement links when scanning campus food & dining QRs, virally pulling peer groups back into Paytm.

### 8. How It Works (Customer Journey)
* **Step 1 [Trigger]:** User taps the lockscreen "Paytm TurboScan" widget at a canteen, tea stall, or kirana counter.
* **Step 2 [Sub-Second Scan]:** Camera launches in <300ms; QR is decoded instantly; biometric confirms payment.
* **Step 3 [Soundbox Sync]:** Merchant Soundbox announces payment; customer app prompts: *"Splitting this bill?"*
* **Step 4 [1-Tap Split Request]:** User selects campus contacts; instant payment links are dispatched.
* **Step 5 [Peer Habituation Loop]:** Friends tap notification and approve payment via Paytm UPI in 1 click.

### 9. Why Users Will Switch (Direct VOC Mapping)
* **Solves Speed Friction ($24.3\%$ barrier):** TurboScan delivers faster tap-to-pay than Google Pay.
* **Intercepts Muscle Memory ($36.9\%$ barrier):** OS-level lockscreen shortcut breaks rival opening habits.
* **Overcomes Peer Lock-in ($25.2\%$ driver):** SplitPass makes Paytm the default campus group ledger.
* **Eliminates Clutter:** Isolates payment flow from banners, loans, and non-payment services.

### 10. Why Paytm Wins (Unfair Ecosystem Advantages)
* **Soundbox Physical Presence:** Paytm owns the merchant checkout counter; integrating customer SplitPass with merchant Soundboxes creates a proprietary two-sided verification loop rivals cannot replicate.
* **Zero Acquisition Cost:** $57.5\%$ of non-primary users already have active Paytm UPI bank accounts linked.
* **Full-Stack Monetization Funnel:** Once daily frequency is captured, Paytm seamlessly cross-sells Co-Branded Credit Cards, Student Travel, Fastag, and Wealth products.

### 11. Expected Business Impact (12-Month Horizon)
* **Incremental MTUs:** $+2.48\text{ Million}$ Monthly Transacting Users.
* **Monthly GMV Growth:** $+₹437.2\text{ Crore / Month}$ ($+₹5,246\text{ Cr}$ Annual Run-Rate).
* **Average User Frequency:** Increases from $1.8$ to $9.8$ transactions per active youth user per month.
* **Paytm UPI Market Share:** $+3.8\%$ to $+4.5\%$ overall UPI market share gain in youth & merchant P2M.

### 12. Measurement KPIs & Scalability
1. **Scan-to-Confirmation Latency:** Target $<1.2$ seconds end-to-end.
2. **Lockscreen Scanner Default Rate:** $>35\%$ of merchant scans executed via TurboScan widget.
3. **Viral Split Settlement Ratio:** $>70\%$ of SplitPass requests completed within 60 minutes.
4. **Horizontal Scalability:** Expand beyond campuses to corporate food courts, metro transit, and supermarket retail.
"""

with open(os.path.join(base_dir, "submission/executive_summary/Paytm_Innovation_Challenge_Executive_Summary.md"), "w", encoding="utf-8") as f:
    f.write(exec_md)

# Copy DOCX report to submission/executive_summary
shutil.copy2(os.path.join(base_dir, "Paytm_Innovation_Challenge_2026_VOC_Research_Report.docx"), os.path.join(base_dir, "submission/executive_summary/Paytm_Innovation_Challenge_2026_VOC_Research_Report.docx"))

# 2. Supporting Evidence: Verbatims Matrix
verb_md = """# Authentic Voice-of-Customer Verbatims Traceability Matrix
**Data Source:** `Paytm_VOC_Authoritative_Final_Dataset.csv` (`VIRTUS_001` to `VIRTUS_113`)  
**Methodology:** 100% genuine verbatim responses extracted directly from the surveyed dataset.

| Respondent ID | Profile | Location | Stated Primary App | Paytm 90d Active | Exact Respondent Verbatim | Strategic Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **VIRTUS_040** | College student | Sitapur (UP) | Google Pay | Yes | *"I can use Paytm often, but i Gpay more, maybe because it is easier to use GPay than Paytm"* | Proves that perceived cognitive ease and tap-latency dictate daily checkout default. |
| **VIRTUS_022** | Working pro | Lucknow (UP) | Google Pay | Yes | *"If Paytm offered faster payments and better rewards, I would use it more often."* | High-frequency power user demanding speed at counter checkout. |
| **VIRTUS_025** | College student | Sitapur (UP) | Google Pay | No | *"If my friend used it more"* | Direct evidence of P2P network lock-in forcing app choice. |
| **VIRTUS_076** | College student | Sitapur (UP) | PhonePe | No | *"अगर मेरे दोस्त और परिचित इसका अधिक उपयोग करते।"* | Language-agnostic peer dependency across Tier 2/3 youth. |
| **VIRTUS_056** | Working pro | Bhopal (MP) | PhonePe | No | *"Make paytm options. Like phonepe, big and easy"* | Demands uncluttered, bold payment buttons for quick counter scan. |
| **VIRTUS_066** | Other | Sitapur (UP) | PhonePe | Yes | *"If Paytm made my daily payments faster and easier, I would use it more."* | Active Paytm user demanding operational speed in daily routines. |
| **VIRTUS_104** | Working pro | Bengaluru (KA) | CRED | No | *"If their wallet system is back again, as PayTm is widely accepted."* | Highlights Paytm's formidable offline merchant acceptance footprint. |
| **VIRTUS_007** | Working pro | Bhopal (MP) | Paytm | Yes | *"Daily payment can manage very easy"* | Validates strong retention once the daily payment habit is established. |
| **VIRTUS_020** | College student | Bhopal (MP) | Google Pay | No | *"Better offers and returns. When it can become more than just a payment app maybe."* | Youth seeking integrated ecosystem utility beyond scratchcards. |
| **VIRTUS_017** | College student | Sitapur (UP) | Slice | Yes | *"Clean ui"* | Reinforces aesthetic demand for minimalism among Gen-Z users. |
| **VIRTUS_029** | Other | Sitapur (UP) | Google Pay | No | *(Contradictory)* *"Kuchh achchha reward milega to use karuga vaese maine Google par bharosa karke hi gpay use karna start kiya h aur kisi pr bharosa nhi"* | Baseline trust barrier in older non-tech cohorts requiring bank-grade reassurance. |
"""

with open(os.path.join(base_dir, "submission/supporting_evidence/VOC_Verbatims_Traceability_Matrix.md"), "w", encoding="utf-8") as f:
    f.write(verb_md)

# 3. Supporting Evidence: Financial Model
fin_md = """# Financial Business Impact & Unit Economics Model

## 1. Mathematical Formulation
$$\\text{Incremental Monthly GMV} = \\text{Target Converted MTUs} \\times \\Delta \\text{ Monthly Transactions} \\times \\text{Blended Offline AOV}$$

## 2. Sensitivity Scenarios (12-Month Horizon)
| Scenario | MTU Conversion Rate | Converted MTUs | Monthly Freq Shift | Blended AOV | Incremental Monthly GMV | Incremental Annual GMV |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Conservative** | $8.0\%$ | $1,324,800$ | $+5$ txns/mo | ₹$180$ | **₹$119.2\\text{ Crore}$** | **₹$1,430.8\\text{ Crore}$** |
| **Base Case** | **$15.0\%$** | **$2,484,000$** | **$+8$ txns/mo** | **₹$220$** | **₹$437.2\\text{ Crore}$** | **₹$5,246.2\\text{ Crore}$** |
| **Aggressive** | $25.0\%$ | $4,140,000$ | $+12$ txns/mo | ₹$260$ | **₹$1,291.7\\text{ Crore}$** | **₹$15,500.2\\text{ Crore}$** |

## 3. Parameter Inputs & Assumptions
1. **Target Addressable Base (45M Youth):** India college student and young urban smartphone transactor population (Ages 18–26).
2. **Paytm Active Penetration ($64.0\%$ Observed):** 28.8M registered youth users with active Paytm credentials.
3. **Non-Defaulting Target Base ($57.5\%$ Observed):** 16.56M active Paytm users currently opening Google Pay or PhonePe.
4. **Blended Offline AOV (₹220):** Observed ticket sizes across campus food (₹80), kirana groceries (₹250), retail (₹650), and transit (₹50).
"""

with open(os.path.join(base_dir, "submission/supporting_evidence/Financial_Business_Impact_Model.md"), "w", encoding="utf-8") as f:
    f.write(fin_md)

print("Generated all final submission documents.")
