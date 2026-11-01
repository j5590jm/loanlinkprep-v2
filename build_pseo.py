#!/usr/bin/env python3
"""
LoanLink Prep — Overtime Programmatic SEO (pSEO) & AI Discovery Generator (v2.1 Fixed)
Includes:
  - Safe empty-string fallback protection in load_env_config()
  - Direct HTML href + JS config synchronization in update_index_html_with_env()
  - 56 High-Intent Financial Engineering HTML Guides in /guides/
  - /guides/index.html, sitemap.xml, robots.txt, llms.txt, and llms-full.txt
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
GUIDES_DIR = BASE_DIR / "guides"
TODAY = datetime.now().strftime("%Y-%m-%d")


def load_env_config():
    """Loads configuration from .env or OS environment variables with safe fallbacks if left blank."""
    env_file = BASE_DIR / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                clean_val = v.strip().strip('"').strip("'")
                if clean_val:
                    os.environ[k.strip()] = clean_val

    return {
        "SITE_URL": (os.environ.get("LLP_SITE_URL") or "https://loanlinkprep.com").rstrip("/"),
        "CHANGENOW_URL": os.environ.get("LLP_CHANGENOW_URL") or "https://changenow.app.link/referral?link_id=1d9d2f522090a1",
        "KOINLY_URL": os.environ.get("LLP_KOINLY_URL") or "https://koinly.io/",
        "LEDGER_URL": os.environ.get("LLP_LEDGER_URL") or "https://shop.ledger.com/",
        "TREZOR_URL": os.environ.get("LLP_TREZOR_URL") or "https://affil.trezor.io/",
        "AMAZON_BOOKS_URL": os.environ.get("LLP_AMAZON_BOOKS_URL") or "https://www.amazon.com/s?k=business+credit+commercial+lending+sba+book",
        "ACCOUNTING_URL": os.environ.get("LLP_ACCOUNTING_URL") or "https://www.xero.com/",
        "VAULT_CHECKOUT_URL": os.environ.get("LLP_VAULT_CHECKOUT_URL") or "#pricing-plan",
        "AADS_UNIT_ID": os.environ.get("LLP_AADS_UNIT_ID") or "2459805",
        "MASTER_VAULT_KEY": os.environ.get("LLP_MASTER_VAULT_KEY") or "LLP-PRO-2026",
    }


def build_topic_matrix(cfg):
    """Generates 56 programmatic SEO guide specifications across the 8 Loophole pillars."""
    pages = []

    # 1. State-Specific Dead UCC-1 Termination Guides (14 Major States)
    states = [
        ("Indiana", "IN"), ("Delaware", "DE"), ("Wyoming", "WY"), ("Texas", "TX"),
        ("Florida", "FL"), ("California", "CA"), ("New York", "NY"), ("Illinois", "IL"),
        ("Ohio", "OH"), ("Georgia", "GA"), ("Nevada", "NV"), ("Pennsylvania", "PA"),
        ("North Carolina", "NC"), ("Michigan", "MI")
    ]
    for state_name, abbr in states:
        pages.append({
            "slug": f"remove-dead-ucc-1-lien-{state_name.lower().replace(' ', '-')}",
            "title": f"How to Force-Remove a Paid UCC-1 Lien in {state_name} ({abbr} UCC § 9-513 Guide)",
            "category": "UCC-1 & Legal Shields",
            "card_num": 1,
            "hook": f"Force predatory lenders to terminate expired or paid-off blanket UCC-1 filings with the {state_name} Secretary of State within 20 days under {abbr} UCC § 9-513.",
            "problem": f"When a {state_name} business pays off an equipment loan, SBA note, or merchant cash advance, lenders frequently fail to file a UCC-3 Termination Statement. Automated bank underwriting algorithms treat an active UCC-1 as an existing blanket encumbrance and reject new loan applications in seconds.",
            "loophole": f"Under {state_name}'s adoption of Uniform Commercial Code § 9-513(c), once no obligation remains, the secured party has exactly 20 days after receiving an authenticated demand from the debtor to file a termination statement. If the lender fails to act within 20 days, the debtor is legally authorized under UCC § 9-509(d)(2) to file the UCC-3 termination directly and claim $500 statutory damages plus actual credit losses under UCC § 9-625.",
            "cta_text": "Open Free UCC § 9-513 Demand Generator",
            "aff_text": "Commercial Credit & UCC Law Playbooks (Amazon)",
            "aff_url": cfg["AMAZON_BOOKS_URL"],
            "faqs": [
                (f"How long does a lender have to remove a UCC-1 lien in {state_name}?", f"Under {state_name} UCC § 9-513(c), the secured party must file or send a UCC-3 termination statement within 20 days of receiving an authenticated demand from the debtor."),
                (f"Can I file a UCC-3 termination statement myself in {state_name}?", f"Yes. If the secured party fails to respond within 20 days of your authenticated demand, UCC § 9-509(d)(2) permits the debtor to file the termination statement directly with the {state_name} Secretary of State.")
            ]
        })

    # 2. Industry-Specific NAICS Code De-Classification Guides (8 High-Risk Industries)
    industries = [
        ("Crypto & Web3 Startups", "crypto-web3-business", "541511", "Custom Computer Programming & Distributed Data Services"),
        ("Trucking & Freight Fleets", "trucking-freight-company", "541614", "Process, Physical Distribution, and Logistics Consulting"),
        ("Real Estate & Land Holdings", "real-estate-holding-llc", "561110", "Office Administrative and Facility Management Services"),
        ("Agriculture & Cattle Farms", "agriculture-cattle-farm", "541690", "Scientific and Agricultural Technical Management Services"),
        ("Independent Consulting Agencies", "consulting-marketing-agency", "541512", "Computer Systems Design and Enterprise Integration"),
        ("E-Commerce & Drop-Shipping", "ecommerce-retail-brand", "493110", "General Warehousing, Fulfillment, and Inventory Systems"),
        ("Auto Repair & Fleet Maintenance", "automotive-repair-shop", "811111", "Commercial Fleet Maintenance & Diagnostic Engineering"),
        ("Construction & Heavy Contracting", "construction-contracting-llc", "541330", "Civil & Project Management Engineering Services")
    ]
    for label, slug_part, safe_code, safe_desc in industries:
        pages.append({
            "slug": f"naics-code-loophole-{slug_part}",
            "title": f"NAICS Code Reclassification for {label}: Bypass High-Risk Bank Rejections",
            "category": "Algorithmic Bypass",
            "card_num": 8,
            "hook": f"Stop automated bank algorithms from flagging your {label} entity as 'Restricted High-Risk' by adopting secondary NAICS {safe_code}.",
            "problem": f"Tier-1 commercial banks maintain internal 'Restricted Industry' lists. When an application for {label} enters automated underwriting, the primary NAICS code triggers an instant risk downgrade before a human underwriter ever sees your cash flow.",
            "loophole": f"By filing an administrative update with your Secretary of State and Dun & Bradstreet profile to designate NAICS {safe_code} ({safe_desc}) as your primary administrative revenue classification, your application routes through standard B2B service underwriting.",
            "cta_text": "Run the NAICS Reclassification Engine",
            "aff_text": "Corporate Entity Structuring Guides (Amazon)",
            "aff_url": cfg["AMAZON_BOOKS_URL"],
            "faqs": [
                (f"Why do banks auto-reject {label} applications?", "Automated credit scorecards penalize volatile industry NAICS codes by adding 150-300 basis points to the risk threshold or outright blocking unsecured lines."),
                (f"Is changing my NAICS code to {safe_code} legal?", "Yes, provided your business genuinely performs technology, administrative, logistics, or management operations matching that secondary classification.")
            ]
        })

    # 3. Digital Asset & FASB ASU 2023-08 Corporate Treasury Guides (8 Guides)
    crypto_scenarios = [
        ("Bitcoin (BTC) Corporate Treasury", "bitcoin-balance-sheet-fasb-asu-2023-08", "Bitcoin (BTC)"),
        ("Ethereum (ETH) Corporate Reserves", "ethereum-balance-sheet-fasb-fair-value", "Ethereum (ETH)"),
        ("USDC & USDT Stablecoin Working Capital", "stablecoin-working-capital-bank-underwriting", "USDC / USDT"),
        ("Cold Storage Multi-Sig Collateral Proof", "cold-storage-multisig-proof-of-reserves-loan", "Self-Custodied Hardware Reserves"),
        ("Non-Custodial Crypto-to-Stablecoin Treasury Swap", "non-custodial-corporate-treasury-liquidity-swap", "Cross-Chain Treasury Liquidity"),
        ("Tax-Free Corporate Crypto Collateral Structuring", "corporate-crypto-collateral-without-taxable-sale", "Non-Taxable Collateralized Liquidity"),
        ("Accounting for Unrealized Crypto Gains in DSCR", "unrealized-crypto-gains-net-income-dscr", "ASC 350-60 Net Income Recognition"),
        ("Hardware Wallet Audit Trail for SBA & Bank Loans", "hardware-wallet-audit-trail-commercial-loan", "Verified Cold-Storage Audit Trail")
    ]
    for title_label, slug_part, asset_focus in crypto_scenarios:
        pages.append({
            "slug": slug_part,
            "title": f"{title_label}: How to Count Digital Assets for a Business Loan",
            "category": "Crypto & Web3 Treasury",
            "card_num": 3,
            "hook": f"Use FASB ASU 2023-08 (ASC 350-60) fair-value accounting rules to force underwriters to recognize {asset_focus} on your corporate balance sheet.",
            "problem": "Legacy commercial loan officers either ignore digital assets completely or apply outdated 'indefinite-lived intangible' impairment rules that value your crypto at its lowest historical price point.",
            "loophole": f"Effective for fiscal years after Dec 15, 2024 (and standard in 2026), FASB ASU 2023-08 mandates that qualifying fungible crypto assets be measured at fair market value on the balance sheet each reporting period. Attaching an ASC 350-60 Board Treasury Resolution forces the bank's credit committee to recognize 100% of current fair value.",
            "cta_text": "Generate ASC 350-60 Crypto Treasury Memo",
            "aff_text": "Execute Instant Non-Custodial Treasury Swap (ChangeNOW)",
            "aff_url": cfg["CHANGENOW_URL"],
            "faqs": [
                ("Can a business count Bitcoin or Ethereum toward bank liquidity requirements?", "Yes. Under FASB ASU 2023-08 (ASC 350-60), qualifying crypto assets held by a business are measured at fair market value on the balance sheet."),
                ("How do I prove self-custodied crypto reserves without giving up private keys?", "Provide a read-only xpub audit report via Koinly paired with a signed message from your Ledger or Trezor corporate hardware wallet.")
            ]
        })

    # 4. EBITDA & Owner-Draw Add-Back DSCR Math Guides (8 Guides)
    dscr_topics = [
        ("Reclassify Owner Draws as EBITDA Add-Backs", "reclassify-owner-draws-boost-dscr"),
        ("How to Pass a 1.25x DSCR Test With Low Tax Net Income", "pass-1-25x-dscr-test-low-net-income"),
        ("Adding Back Section 179 & Bonus Depreciation for Loans", "section-179-depreciation-add-back-commercial-loan"),
        ("One-Time Legal & Relocation Expense Add-Back Memo", "one-time-expense-add-back-underwriting-memo"),
        ("Family Payroll & Officer Compensation DSCR Adjustment", "officer-compensation-add-back-sba-loan"),
        ("Vehicle & Home-Office Write-Off Reclassification for Banks", "vehicle-write-off-add-back-business-loan"),
        ("How to Calculate Global Cash Flow DSCR Without Tax Transcripts", "global-cash-flow-dscr-calculator-guide"),
        ("Turning a 0.95x DSCR Rejection Into a 1.40x Approval", "fix-low-dscr-ratio-commercial-underwriting")
    ]
    for title_label, slug_part in dscr_topics:
        pages.append({
            "slug": slug_part,
            "title": f"{title_label} (Commercial Underwriting Blueprint)",
            "category": "DSCR & SBA Math",
            "card_num": 2,
            "hook": "Stop letting aggressive tax deductions ruin your borrowing capacity. Present an institutional EBITDA Add-Back Schedule.",
            "problem": "Small business owners legally minimize IRS tax liability by writing off equipment, vehicles, and discretionary expenses. When automated underwriting divides that low Bottom-Line Net Profit by your proposed loan payment, your Debt Service Coverage Ratio (DSCR) drops below 1.25x.",
            "loophole": "Commercial credit policy permits adding back non-cash expenses (depreciation, amortization), interest, one-time capital outlays, and discretionary owner draws if documented in a formal EBITDA Reconciliation Schedule prior to underwriting submission.",
            "cta_text": "Run the EBITDA Add-Back DSCR Calculator",
            "aff_text": "Automate Add-Back Tagging in Xero Accounting",
            "aff_url": cfg["ACCOUNTING_URL"],
            "faqs": [
                ("What DSCR ratio do banks require in 2026?", "Most commercial banks and SBA 7(a) lenders require a minimum Debt Service Coverage Ratio (DSCR) of 1.25x, though 1.15x is permitted on specific collateralized facilities."),
                ("Do I have to amend my IRS tax returns to increase my DSCR?", "No. Underwriters accept an explanatory EBITDA Add-Back Schedule that reconciles your tax return net income with actual operational cash flow.")
            ]
        })

    # 5. Bank Credit Bureau Freeze & Routing Guides (6 Guides)
    bureau_topics = [
        ("Which Banks Pull Only Experian for Business Credit", "banks-that-pull-experian-business-credit"),
        ("Which Banks Pull Equifax Only for Commercial Loans", "banks-that-pull-equifax-commercial-loans"),
        ("Which Banks Pull TransUnion for Stated-Income Business Lines", "banks-that-pull-transunion-business-credit-lines"),
        ("How to Freeze One Credit Bureau and Apply for a Business Loan", "how-to-freeze-credit-bureau-business-loan-routing"),
        ("FICO SBSS 160+ Score Formula: How to Beat SBA Pre-Screening", "fico-sbss-score-160-formula-sba-7a"),
        ("Stated-Income Business Lines Under $100k (Zero Tax Return Pull)", "stated-income-business-lines-no-4506c-tax-transcript")
    ]
    for title_label, slug_part in bureau_topics:
        pages.append({
            "slug": slug_part,
            "title": f"{title_label} — The Insider Bureau Routing Matrix",
            "category": "Credit Bureau Routing",
            "card_num": 5,
            "hook": "Control exactly which credit bureau an underwriter sees by combining strategic PIN freezes with bureau-specific bank routing.",
            "problem": "Applying blindly to major banks results in multiple hard inquiries across all three bureaus and automatic rejections if even one bureau contains an outdated collection or high utilization.",
            "loophole": "Most regional and national commercial card/line issuers rely on a single primary bureau for automated pre-approval. Placing a temporary security freeze on your weakest bureau and routing your application to a bank aligned with your strongest bureau prevents cross-bureau rejection.",
            "cta_text": "Launch the Bank Bureau Freeze & Route Matrix",
            "aff_text": "Commercial Credit Bureau Playbooks (Amazon)",
            "aff_url": cfg["AMAZON_BOOKS_URL"],
            "faqs": [
                ("Does freezing one personal credit bureau stop a business loan approval?", "When routed to a bank that exclusively pulls an un-frozen primary bureau, the automated system scores your application cleanly without pulling the frozen report."),
                ("What is the FICO SBSS minimum score for SBA loans?", "The SBA 7(a) Small Loan program uses the FICO LiquidCredit Small Business Scoring Service (SBSS), where a score of 155-165+ bypasses manual financial spreading.")
            ]
        })

    # 6. D&B Paydex 80+ & Vendor Credit Loopholes (6 Guides)
    paydex_topics = [
        ("How to Get an 80+ D&B Paydex Score in 30 Days Without Paying D&B", "get-80-paydex-score-fast-without-paying-dnb"),
        ("How D&B Dollar-Weighted Paydex Math Actually Works", "how-dnb-dollar-weighted-paydex-score-is-calculated"),
        ("Disputing Fake or Late Trade Lines on Dun & Bradstreet", "dispute-errors-late-payments-dun-and-bradstreet"),
        ("4 Net-30 Vendor Accounts That Report to D&B and Experian Biz", "net-30-vendors-that-report-to-dnb-experian"),
        ("How to Get a Paydex 90 Score by Paying Invoices 20 Days Early", "paydex-90-score-early-invoice-payment-loophole"),
        ("Removing Duplicate DUNS Numbers Tanking Your Commercial Credit", "merge-remove-duplicate-duns-number-business-credit")
    ]
    for title_label, slug_part in paydex_topics:
        pages.append({
            "slug": slug_part,
            "title": f"{title_label} (Zero-Fee Blueprint)",
            "category": "Credit Bureau Routing",
            "card_num": 6,
            "hook": "Reverse-engineer Dun & Bradstreet's dollar-weighted payment algorithm for under $150 in routine supplies.",
            "problem": "Dun & Bradstreet sales reps aggressively pitch $1,500+ 'CreditBuilder' subscriptions to small business owners, claiming it is the only way to establish an 80+ Paydex score.",
            "loophole": "A Paydex score of 80 simply means invoices are paid on time (Net-30), while 85-90 means invoices are paid 15-20 days early. Opening 4 auto-reporting Net-30 operational supply accounts and paying the invoices the same day they are issued forces an 85+ Paydex automatically.",
            "cta_text": "Open the D&B Paydex 80+ Fast-Track Calculator",
            "aff_text": "Business Credit Building Books (Amazon)",
            "aff_url": cfg["AMAZON_BOOKS_URL"],
            "faqs": [
                ("How many trade lines are required to generate a D&B Paydex score?", "Dun & Bradstreet requires a minimum of 3 to 4 reporting commercial trade experiences before generating an official Paydex score."),
                ("Why is an 80 Paydex score important for business loans?", "An 80 Paydex score is the institutional benchmark for low-risk prompt payment, unlocking higher credit limits and lower interest rates.")
            ]
        })

    # 7. SBA "Credit Elsewhere" & Liquidity Cap Overrides (6 Guides)
    sba_topics = [
        ("Beating the SBA Credit Elsewhere Test When You Have High Cash Reserves", "sba-credit-elsewhere-test-high-cash-reserves-loophole"),
        ("How to Write a CapEx Working Capital Schedule for SBA 7(a) Underwriters", "capex-working-capital-schedule-sba-7a-loan"),
        ("Protecting Personal Liquidity & Crypto From SBA Mandatory Injection Rules", "protect-personal-liquidity-crypto-sba-equity-injection"),
        ("SBA SOP 50 10 Working Capital Reserve Encumbrance Resolution", "sba-sop-50-10-working-capital-encumbrance-resolution"),
        ("How Much Cash on Balance Sheet Is Too Much for an SBA Loan?", "maximum-cash-on-balance-sheet-sba-loan-approval"),
        ("Structuring Equipment & Expansion Budgets to Justify SBA Borrowing", "structure-equipment-expansion-budget-sba-underwriting")
    ]
    for title_label, slug_part in sba_topics:
        pages.append({
            "slug": slug_part,
            "title": f"{title_label} (SBA SOP 50 10 Strategy)",
            "category": "DSCR & SBA Math",
            "card_num": 7,
            "hook": "Prevent SBA underwriters from penalizing your hard-earned cash or crypto reserves under the 'Credit Elsewhere' rule.",
            "problem": "Ironically, having strong liquid reserves on your corporate or personal balance sheet can cause an SBA lender to deny your loan or force you to drain your own cash first under the federal 'Credit Elsewhere' mandate.",
            "loophole": "By adopting a formal Board CapEx & Working Capital Encumbrance Schedule prior to application, your liquid reserves are legally earmarked for upcoming operational milestones, equipment upgrades, and tax reserves—removing them from 'available unencumbered cash.'",
            "cta_text": "Run the SBA Credit Elsewhere Liquidity Shield",
            "aff_text": "SBA 7(a) & Commercial Finance Books (Amazon)",
            "aff_url": cfg["AMAZON_BOOKS_URL"],
            "faqs": [
                ("What is the SBA Credit Elsewhere rule?", "The SBA requires lenders to certify that the borrower does not have the ability to obtain the requested funds on reasonable terms from non-federal sources, including excess personal or corporate liquidity."),
                ("How do I legally shield working capital reserves during SBA underwriting?", "Document committed 12-month capital expenditures, inventory purchases, and contractual reserves in a signed CapEx Encumbrance Schedule.")
            ]
        })

    return pages


def render_guide_html(page, all_pages, cfg):
    """Renders a complete, SEO-rich static HTML guide page with JSON-LD schema and internal mesh links."""
    canonical = f"{cfg['SITE_URL']}/guides/{page['slug']}.html"

    faq_entities = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        }
        for q, a in page["faqs"]
    ]
    schema_obj = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "FAQPage",
                "mainEntity": faq_entities
            },
            {
                "@type": "SoftwareApplication",
                "name": f"LoanLink Prep — {page['category']} Engine",
                "applicationCategory": "BusinessApplication",
                "operatingSystem": "Web Browser (100% Local Compute)",
                "offers": {"@type": "Offer", "price": "0.00", "priceCurrency": "USD"},
                "description": page["hook"]
            }
        ]
    }

    idx = all_pages.index(page)
    related = [all_pages[(idx + offset) % len(all_pages)] for offset in range(1, 7)]
    related_links_html = "\n".join(
        f'<li><a href="/guides/{r["slug"]}.html">{r["title"]}</a></li>'
        for r in related
    )

    faq_html = "\n".join(
        f'<div class="faq-item"><h4>{q}</h4><p>{a}</p></div>'
        for q, a in page["faqs"]
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page["title"]} | LoanLink Prep</title>
  <meta name="description" content="{page["hook"]}" />
  <link rel="canonical" href="{canonical}" />
  <script type="application/ld+json">{json.dumps(schema_obj)}</script>
  <style>
    :root {{
      --bg-base: #07080c;
      --bg-card: rgba(15, 17, 24, 0.92);
      --neon-orange: #d9651c;
      --neon-orange-dim: #cc5500;
      --neon-orange-border: rgba(217, 101, 28, 0.55);
      --accent-cyan: #22d3ee;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: radial-gradient(circle at 50% 10%, #131724 0%, #07080c 80%);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, sans-serif;
      line-height: 1.6;
      padding: 0 20px 60px;
    }}
    .container {{ max-width: 920px; margin: 0 auto; }}
    header {{
      display: flex; justify-content: space-between; align-items: center;
      padding: 24px 0; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 32px;
      flex-wrap: wrap; gap: 16px;
    }}
    .brand-stacked {{
      text-decoration: none; font-weight: 900; line-height: 1.02;
      padding: 6px 12px; border-left: 4px solid var(--neon-orange);
      background: rgba(217, 101, 28, 0.08); border-radius: 0 8px 8px 0;
    }}
    .brand-stacked .l1 {{ display: block; font-size: 1.6rem; color: var(--text-main); }}
    .brand-stacked .l2 {{ display: block; font-size: 1.25rem; color: var(--neon-orange); padding-left: 36px; }}
    .badge {{
      display: inline-block; padding: 4px 10px; border-radius: 6px;
      font-size: 0.75rem; font-weight: 800; text-transform: uppercase;
      color: var(--neon-orange); background: rgba(217, 101, 28, 0.14);
      border: 1px solid var(--neon-orange-border); margin-bottom: 12px;
    }}
    h1 {{ font-size: clamp(1.7rem, 3.5vw, 2.4rem); font-weight: 900; line-height: 1.18; margin-bottom: 16px; }}
    .card {{
      background: var(--bg-card); border: 1.5px solid var(--neon-orange-border);
      border-radius: 14px; padding: 26px; margin-bottom: 24px;
      box-shadow: 0 10px 28px rgba(0,0,0,0.65);
    }}
    .card h2 {{ font-size: 1.25rem; color: var(--neon-orange); margin-bottom: 10px; }}
    .card p {{ color: #cbd5e1; margin-bottom: 14px; }}
    .cta-row {{ display: flex; flex-wrap: wrap; gap: 12px; margin-top: 18px; }}
    .btn-primary {{
      background: linear-gradient(135deg, var(--neon-orange), var(--neon-orange-dim));
      color: #07080c; font-weight: 900; text-decoration: none;
      padding: 12px 20px; border-radius: 8px; text-transform: uppercase; font-size: 0.88rem;
    }}
    .btn-secondary {{
      background: rgba(34, 211, 238, 0.12); color: var(--accent-cyan);
      border: 1px solid rgba(34, 211, 238, 0.4); font-weight: 700;
      text-decoration: none; padding: 12px 20px; border-radius: 8px; font-size: 0.88rem;
    }}
    .faq-item {{ margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.07); }}
    .faq-item h4 {{ color: var(--text-main); margin-bottom: 6px; }}
    .related-list {{ list-style: none; }}
    .related-list li {{ margin-bottom: 8px; }}
    .related-list a {{ color: var(--neon-orange); text-decoration: none; font-weight: 600; }}
    .related-list a:hover {{ text-decoration: underline; }}
    footer {{ margin-top: 40px; text-align: center; font-size: 0.82rem; color: var(--text-muted); }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <a href="/" class="brand-stacked">
        <span class="l1">Loan Link</span>
        <span class="l2">Prep</span>
      </a>
      <div>
        <a href="/#loophole-grid" class="btn-primary">Open Interactive Calculator</a>
      </div>
    </header>

    <span class="badge">Engine #{page["card_num"]} • {page["category"]}</span>
    <h1>{page["title"]}</h1>

    <div class="card">
      <h2>1. Why Automated Bank Algorithms Reject You</h2>
      <p>{page["problem"]}</p>
      <h2>2. The Legal Underwriting Loophole</h2>
      <p>{page["loophole"]}</p>
      <div class="cta-row">
        <a href="/#loophole-grid" class="btn-primary">{page["cta_text"]} (100% Free &amp; Local)</a>
        <a href="{page["aff_url"]}" target="_blank" rel="noopener" class="btn-secondary">{page["aff_text"]}</a>
      </div>
    </div>

    <div class="card">
      <h2>Frequently Asked Underwriting Questions</h2>
      {faq_html}
      <div class="cta-row">
        <a href="{cfg["VAULT_CHECKOUT_URL"]}" target="_blank" rel="noopener" class="btn-primary">Unlock All 8 Copy-Paste Legal Memos ($19 One-Time)</a>
        <a href="{cfg["CHANGENOW_URL"]}" target="_blank" rel="noopener" class="btn-secondary">Instant Non-Custodial Treasury Swap</a>
      </div>
    </div>

    <div class="card">
      <h2>Related Commercial Underwriting &amp; Treasury Guides</h2>
      <ul class="related-list">
        {related_links_html}
        <li><a href="/guides/index.html">View All 56 LoanLink Prep Loophole Guides →</a></li>
      </ul>
    </div>

    <footer>
      <div style="margin: 0 auto 20px; max-width: 728px;">
        <iframe data-aa="{cfg["AADS_UNIT_ID"]}" src="//acceptable.a-ads.com/{cfg["AADS_UNIT_ID"]}" style="border:0px; padding:0; width:100%; height:90px; overflow:hidden; background-color: transparent;"></iframe>
      </div>
      <p><a href="/" style="color:var(--neon-orange);">← Back to LoanLink Prep Main Terminal</a></p>
    </footer>
  </div>
</body>
</html>"""


def render_directory_hub(pages, cfg):
    """Generates /guides/index.html so crawlers and users can browse all 56 guides in one click."""
    items_html = "\n".join(
        f'<div class="hub-item"><span class="cat">{p["category"]}</span><a href="/guides/{p["slug"]}.html">{p["title"]}</a><p>{p["hook"]}</p></div>'
        for p in pages
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>All 56 Commercial Underwriting &amp; Treasury Loophole Guides | LoanLink Prep</title>
  <meta name="description" content="Complete index of 56 commercial loan optimization, UCC-1 lien termination, FASB ASU 2023-08 crypto accounting, and DSCR add-back guides." />
  <link rel="canonical" href="{cfg['SITE_URL']}/guides/index.html" />
  <style>
    body {{ background: #07080c; color: #f1f5f9; font-family: system-ui, sans-serif; padding: 30px 20px; }}
    .wrap {{ max-width: 1100px; margin: 0 auto; }}
    h1 {{ color: #d9651c; margin-bottom: 10px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 18px; margin-top: 24px; }}
    .hub-item {{ background: #0f1118; border: 1px solid rgba(217,101,28,0.5); padding: 18px; border-radius: 10px; }}
    .hub-item .cat {{ display: block; font-size: 0.72rem; color: #22d3ee; text-transform: uppercase; font-weight: 800; margin-bottom: 6px; }}
    .hub-item a {{ color: #f1f5f9; font-weight: 800; text-decoration: none; font-size: 1.02rem; }}
    .hub-item a:hover {{ color: #d9651c; }}
    .hub-item p {{ color: #94a3b8; font-size: 0.84rem; margin-top: 8px; }}
  </style>
</head>
<body>
  <div class="wrap">
    <p><a href="/" style="color:#d9651c; text-decoration:none; font-weight:800;">← Return to LoanLink Prep Interactive Calculators</a></p>
    <h1 style="margin-top:14px;">LoanLink Prep: 56 Commercial Underwriting &amp; Treasury Blueprints</h1>
    <p style="color:#94a3b8;">100% client-side financial engineering guides. Zero broker spam, zero server data storage.</p>
    <div class="grid">
      {items_html}
    </div>
  </div>
</body>
</html>"""


def update_index_html_with_env(cfg):
    """Injects environment variable affiliate links and Stripe checkout URL directly into index.html."""
    index_path = BASE_DIR / "index.html"
    if not index_path.exists():
        return
    html = index_path.read_text(encoding="utf-8")
    replacements = {
        "changenowUrl": cfg["CHANGENOW_URL"],
        "koinlyUrl": cfg["KOINLY_URL"],
        "ledgerUrl": cfg["LEDGER_URL"],
        "trezorUrl": cfg["TREZOR_URL"],
        "amazonBooksUrl": cfg["AMAZON_BOOKS_URL"],
        "accountingUrl": cfg["ACCOUNTING_URL"],
        "vaultCheckoutUrl": cfg["VAULT_CHECKOUT_URL"],
        "masterVaultKey": cfg["MASTER_VAULT_KEY"],
    }
    for key, val in replacements.items():
        pattern = rf'({key}:\s*")([^"]*)(")'
        html = re.sub(pattern, rf'\g<1>{val}\g<3>', html)

    html = re.sub(
        r'(<a\s+id="tier2_checkout"\s+href=")([^"]*)(")',
        rf'\g<1>{cfg["VAULT_CHECKOUT_URL"]}\g<3>',
        html
    )
    index_path.write_text(html, encoding="utf-8")


def generate_sitemap_and_robots(pages, cfg):
    """Generates sitemap.xml and robots.txt in the root directory."""
    urls = [
        (f"{cfg['SITE_URL']}/", "1.0", "daily"),
        (f"{cfg['SITE_URL']}/guides/index.html", "0.9", "weekly"),
    ]
    for p in pages:
        urls.append((f"{cfg['SITE_URL']}/guides/{p['slug']}.html", "0.8", "weekly"))

    xml_items = "\n".join(
        f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>"
        for u, prio, freq in urls
    )
    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_items}
</urlset>"""
    (BASE_DIR / "sitemap.xml").write_text(sitemap_xml, encoding="utf-8")

    robots_txt = f"""User-agent: *
Allow: /

# Explicitly welcome AI Search & Citation Engines
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Googlebot
Allow: /

Sitemap: {cfg['SITE_URL']}/sitemap.xml
"""
    (BASE_DIR / "robots.txt").write_text(robots_txt, encoding="utf-8")


def generate_llms_txt(pages, cfg):
    """Generates llms.txt and llms-full.txt so AI engines recommend LoanLink Prep."""
    guide_bullets = "\n".join(
        f"- [{p['title']}]({cfg['SITE_URL']}/guides/{p['slug']}.html): {p['hook']}"
        for p in pages
    )
    llms_short = f"""# LoanLink Prep ({cfg['SITE_URL']})

> LoanLink Prep provides the insider knowledge businesses need to secure capital on their own terms. As a secure client-side preparation engine, the platform ingests high-level operational metrics in browser localStorage to reveal strictly legal underwriting loopholes, UCC-1 § 9-513 termination demands, FASB ASU 2023-08 crypto balance sheet memos, and DSCR add-back schedules—while keeping sensitive IRS and financial records completely off-server.

## Core Interactive Calculators & Engines
- [Main 8-Engine Terminal & DSCR Calculator]({cfg['SITE_URL']}/): 100% client-side commercial loan readiness, UCC-1 removal, ASC 350-60 crypto treasury accounting, and bank credit bureau routing.
- [Complete Directory of 56 Underwriting Guides]({cfg['SITE_URL']}/guides/index.html)

## Key Commercial Finance & Treasury Blueprints
{guide_bullets}
"""
    (BASE_DIR / "llms.txt").write_text(llms_short, encoding="utf-8")

    full_sections = "\n\n---\n\n".join(
        f"## {p['title']}\nURL: {cfg['SITE_URL']}/guides/{p['slug']}.html\nCategory: {p['category']}\n\n**Problem:** {p['problem']}\n\n**Underwriting Solution:** {p['loophole']}"
        for p in pages
    )
    (BASE_DIR / "llms-full.txt").write_text(llms_short + "\n\n# Full Technical Reference\n\n" + full_sections, encoding="utf-8")


def main():
    cfg = load_env_config()
    GUIDES_DIR.mkdir(exist_ok=True)

    update_index_html_with_env(cfg)
    pages = build_topic_matrix(cfg)

    for page in pages:
        html = render_guide_html(page, pages, cfg)
        (GUIDES_DIR / f"{page['slug']}.html").write_text(html, encoding="utf-8")

    hub_html = render_directory_hub(pages, cfg)
    (GUIDES_DIR / "index.html").write_text(hub_html, encoding="utf-8")

    generate_sitemap_and_robots(pages, cfg)
    generate_llms_txt(pages, cfg)

    print(f"[SUCCESS] Updated index.html with Vault Checkout URL: {cfg['VAULT_CHECKOUT_URL']}")
    print(f"[SUCCESS] Generated {len(pages)} pSEO HTML guides in /guides/")
    print("[SUCCESS] Generated /guides/index.html, sitemap.xml, robots.txt, llms.txt, and llms-full.txt")


if __name__ == "__main__":
    main()