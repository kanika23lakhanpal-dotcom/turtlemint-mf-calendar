# -*- coding: utf-8 -*-
# Levels 12 to 16

LEVELS_12_TO_16 = [
    # LEVEL 12
    {
        "level_num": 12,
        "level_title": "Taxation of Mutual Funds",
        "level_tagline": "The September 2026 Baseline: Capital Gains, Holding Periods & Section 50AA",
        "phase": "Phase 4: Goal Advisory, Tax & Costs",
        "modules": [
            {
                "module_id": "M12.1",
                "module_title": "Equity & Debt Scheme Taxation Framework",
                "lessons": [
                    {
                        "lesson_id": "L12.01",
                        "title": "Equity Mutual Fund Taxation: STCG @ 20% & LTCG @ 12.5%",
                        "topic": "Post-Finance Act 2024 Equity Tax Rules",
                        "format": "Interactive Capital Gains Tax Calculator",
                        "duration": "15 mins",
                        "subtopics": [
                            "Equity Scheme Definition: Schemes investing ≥65% in domestic equity shares",
                            "Holding Period Threshold: ≤12 months is Short-Term; >12 months is Long-Term",
                            "Short-Term Capital Gains (STCG): Flat 20% tax (+ 4% cess) on units held for 12 months or less",
                            "Long-Term Capital Gains (LTCG): Flat 12.5% tax (+ 4% cess) on gains exceeding ₹1.25 Lakh per financial year",
                            "The ₹1.25 Lakh Annual Exemption: How small retail investors enjoy completely tax-free profits each year"
                        ],
                        "know": "Equity LTCG is taxed at 12.5% above the ₹1.25 Lakh annual statutory exemption threshold.",
                        "understand": "Mutual funds pay zero tax inside the scheme; tax is levied ONLY when the investor actually redeems or switches units.",
                        "do": "Calculate the exact tax liability for a client earning ₹2,00,000 LTCG on Turtlemint Ninja's tax tool.",
                        "say": "\"Equity fund mein har saal ₹1.25 Lakh tak ka profit bilkul tax-free hota hai, upar sirf 12.5% tax lagta hai.\"",
                        "never_claim": "Never claim that mutual funds are 100% tax-free after 1 year (that exemption was abolished in 2018)."
                    },
                    {
                        "lesson_id": "L12.02",
                        "title": "Debt Funds & Section 50AA: The Slab Rate Architecture",
                        "topic": "Specified Mutual Funds Taxation",
                        "format": "Tax Slabs Flowchart + Case Studies",
                        "duration": "14 mins",
                        "subtopics": [
                            "Specified Mutual Funds: Schemes investing ≤35% in domestic equity shares (Pure Debt, Liquid, Overnight)",
                            "Section 50AA Rule: All capital gains are deemed Short-Term and taxed at the investor's individual income tax slab",
                            "Elimination of Indexation: No indexation benefit regardless of holding period (1 year, 5 years, or 10 years)",
                            "The 35% to 65% Hybrid & Gold Bucket: Holding period 24 months for LTCG @ 12.5% without indexation",
                            "Why debt funds still beat FDs: Tax deferral! You pay tax only when redeeming, not every 31st March"
                        ],
                        "know": "Pure debt funds (≤35% equity) are taxed at individual income tax slab rates upon redemption.",
                        "understand": "Unlike bank FDs where TDS and tax apply every year on accrued interest, debt funds defer tax until redemption day.",
                        "do": "Show an investor in the 20% slab how tax deferral in a debt fund beats annual FD compounding taxation.",
                        "say": "\"Debt fund mein jab tak aap paisa nahi nikaalenge, tab tak koi tax nahi lagega—FD ki tarah har saal tax nahi kat-ta.\"",
                        "never_claim": "Never promise indexation benefits on debt mutual funds purchased under the new post-April 2023 / Finance Act rules."
                    },
                    {
                        "lesson_id": "L12.03",
                        "title": "IDCW Payout Taxation & TDS Under Section 194K",
                        "topic": "Dividend Taxation & TDS Thresholds",
                        "format": "Cash Flow vs Net Retention Infographic",
                        "duration": "11 mins",
                        "subtopics": [
                            "IDCW Taxation: Payouts are added directly to the investor's total income and taxed at normal slab rates",
                            "Section 194K TDS: AMC deducts 10% TDS if total IDCW payout exceeds ₹5,000 in a financial year for residents",
                            "Form 15G / 15H: How senior citizens and low-income earners can avoid TDS deduction",
                            "Why SWP is vastly superior to IDCW: SWP attracts capital gains tax (only on profit component), not full slab tax on entire payout",
                            "Annual Information Statement (AIS) & Form 26AS matching: Avoiding IT department mismatch notices"
                        ],
                        "know": "IDCW is taxed at slab rates in investor hands; AMCs deduct 10% TDS if payout exceeds ₹5,000.",
                        "understand": "An investor in the 30% slab loses 30% of their IDCW payout to taxes; an SWP from Growth option saves huge taxes.",
                        "do": "Run a comparison between ₹20,000/month IDCW payout vs ₹20,000/month SWP on Turtlemint Ninja.",
                        "say": "\"Regular income ke liye IDCW se behtar SWP hai, kyunki SWP mein poore paise par nahi, sirf profit portion par tax lagta hai.\"",
                        "never_claim": "Never tell an investor that IDCW payouts are tax-free in their hands."
                    }
                ]
            }
        ]
    },

    # LEVEL 13
    {
        "level_num": 13,
        "level_title": "Costs & Charges",
        "level_tagline": "The Math of Frictional Loss: TER, Exit Loads & Stamp Duty",
        "phase": "Phase 4: Goal Advisory, Tax & Costs",
        "modules": [
            {
                "module_id": "M13.1",
                "module_title": "Total Expense Ratio (TER) & Transaction Friction",
                "lessons": [
                    {
                        "lesson_id": "L13.01",
                        "title": "Decoding TER: What Does the Scheme Charge?",
                        "topic": "Operating Expenses & SEBI Caps",
                        "format": "Pipeline Siphon Explainer Video",
                        "duration": "13 mins",
                        "subtopics": [
                            "What is TER? Total annual operating cost charged to the scheme, expressed as a daily percentage of AUM",
                            "What goes into TER? Fund management fee, registrar fees, custodian charges, audit, legal, and distributor commission",
                            "SEBI Regulatory Slabs: How TER legally drops as a scheme's AUM grows larger",
                            "Daily NAV Adjustment: How the expense ratio is deducted silently every day before publishing NAV",
                            "Net Returns Reality: When an AMC says the fund gave 15%, that is ALREADY NET of all expense ratio fees!"
                        ],
                        "know": "All published mutual fund returns and NAVs are already net of the Total Expense Ratio (TER).",
                        "understand": "The customer never receives a separate bill or invoice for TER; it is factored into daily NAV calculation.",
                        "do": "Locate the TER of both Direct and Regular plans on a scheme factsheet on Turtlemint Pro.",
                        "say": "\"Jo return aapko screen par dikhta hai, woh saare kharche katne ke baad ka net return hota hai.\"",
                        "never_claim": "Never tell a client that mutual funds charge zero management fees or that distribution is 'completely free'."
                    },
                    {
                        "lesson_id": "L13.02",
                        "title": "Exit Loads, Stamp Duty & Securities Transaction Tax (STT)",
                        "topic": "Entry, Premature Exit & Government Levies",
                        "format": "Fee Invoice Breakdown Interactive",
                        "duration": "12 mins",
                        "subtopics": [
                            "What is an Exit Load? A contractual charge to discourage premature redemptions (e.g., 1% if redeemed within 365 days)",
                            "Where does Exit Load go? It is NOT kept by the AMC or DP—it is credited back into the scheme to benefit remaining investors!",
                            "Stamp Duty: 0.005% levied by the Central Government on all mutual fund purchase transactions since July 2020",
                            "Securities Transaction Tax (STT): 0.001% deducted upon redemption of equity-oriented mutual fund units",
                            "The ₹100 Rule: Calculating exact stamp duty on a ₹1,00,000 investment (Exactly ₹4.98 deducted before unit allotment)"
                        ],
                        "know": "Exit load is paid back into the scheme fund pool; stamp duty is 0.005% on all purchase transactions.",
                        "understand": "Explaining the 1-year exit load upfront prevents customers from treating long-term equity funds like 3-month savings accounts.",
                        "do": "Calculate the net units allotted on a ₹50,000 purchase after stamp duty deduction on Turtlemint Ninja.",
                        "say": "\"Exit load koi penalty nahi hai, yeh lambe samay ke investors ko protect karne ke liye banaya gaya rule hai.\"",
                        "never_claim": "Never promise a client that exit loads can be waived off or refunded by the DP or AMC."
                    }
                ]
            }
        ]
    },

    # LEVEL 14
    {
        "level_num": 14,
        "level_title": "Customer Discovery & Profiling",
        "level_tagline": "The Diagnostic Interview: Asking Questions Like an Empathetic Physician",
        "phase": "Phase 5: Field Mastery — Customer Discovery, Pitch & Compliance",
        "modules": [
            {
                "module_id": "M14.1",
                "module_title": "The Diagnostic Discovery Protocol",
                "lessons": [
                    {
                        "lesson_id": "L14.01",
                        "title": "The 5 Core Discovery Questions",
                        "topic": "The Diagnostic Fact-Finding Protocol",
                        "format": "Doctor Consultation Roleplay Video",
                        "duration": "15 mins",
                        "subtopics": [
                            "Why bad distributors pitch products immediately: The stethoscope vs the medicine salesman",
                            "Question 1: 'Aap yeh paisa kis specific family goal ke liye jod rahe hain?' (Purpose)",
                            "Question 2: 'Aapko is paise ki zaroorat kitne saal baad padegi?' (Time Horizon)",
                            "Question 3: 'Agar market kal 10% gir jaaye, toh aapko kaisa feel hoga?' (Emotional Tolerance)",
                            "Question 4: 'Aapke paas emergency ke liye kitna paisa alag se bank mein rakha hai?' (Emergency Cushion)",
                            "Question 5: 'Aapki monthly savings capacity kitni hai jo bina ruke agle 5 saal chal sake?' (Cash Flow Reality)"
                        ],
                        "know": "A distributor must never recommend a product without first discovering goal, horizon, and liquidity cushion.",
                        "understand": "When you ask diagnostic questions, the customer views you as a trusted professional advisor, not a pushy salesman.",
                        "do": "Complete the Turtlemint 5-question digital discovery checklist before opening the scheme catalog.",
                        "say": "\"Pehle main aapke parivaar ke goals samajhna chahta hoon, uske baad hi hum sahi product ki baat karenge.\"",
                        "never_claim": "Never start a customer meeting by opening a brochure or factsheet and pitching a specific scheme."
                    },
                    {
                        "lesson_id": "L14.02",
                        "title": "Mapping the Financial Baseline: Assets, Debts & Emergency Buffers",
                        "topic": "Evaluating Client Balance Sheet Health",
                        "format": "Interactive Household Balance Sheet Template",
                        "duration": "13 mins",
                        "subtopics": [
                            "Evaluating existing commitments: Home loans, car EMIs, personal loans, insurance premiums",
                            "The Emergency Rule: Ensuring 3 to 6 months of living expenses exist in liquid bank accounts before starting equity SIPs",
                            "Checking existing investments: EPF, PPF, Life insurance traditional plans, physical gold, existing FDs",
                            "Identifying surplus cash: Total monthly income minus mandatory expenses minus loan EMIs = True Investable Surplus",
                            "Preventing over-commitment: Why starting with a comfortable ₹3,000 SIP is 10x better than an aggressive ₹15,000 SIP that stops in 6 months"
                        ],
                        "know": "A client without an emergency fund will be forced to redeem their equity SIP at a loss during a medical crisis.",
                        "understand": "Sizing the SIP conservatively guarantees continuity; high-pressure over-commitment leads to early defaults.",
                        "do": "Fill out a sample Turtlemint Household Financial Profile for a salaried customer earning ₹60,000/month.",
                        "say": "\"Emergency fund pehle banayenge, taaki kal koi zaroorat pade toh mutual fund ko todna na pade.\"",
                        "never_claim": "Never push a client to invest their emergency hospital fund into equity mutual funds."
                    }
                ]
            }
        ]
    },

    # LEVEL 15
    {
        "level_num": 15,
        "level_title": "Master Customer Conversations & Objections",
        "level_tagline": "Real Field Dialogues: 15 Everyday Scenarios Handled with Empathy & Integrity",
        "phase": "Phase 5: Field Mastery — Customer Discovery, Pitch & Compliance",
        "modules": [
            {
                "module_id": "M15.1",
                "module_title": "The Big Indian Household Objections",
                "lessons": [
                    {
                        "lesson_id": "L15.01",
                        "title": "Dialogue 1: 'Mutual Fund Safe Hai Ya Paisa Doob Jayega?'",
                        "topic": "Handling the Ultimate Fear of Capital Loss",
                        "format": "Full Verbatim Audio-Video Script",
                        "duration": "14 mins",
                        "subtopics": [
                            "Understanding the root emotion: The fear of fly-by-night chit funds and speculative stock market scams",
                            "The SEBI & Custodian Armor: Explaining that the AMC cannot steal your money",
                            "The 50 Companies Defense: 'Agar ek company band ho sakti hai, toh kya desh ki top 50 companiyan ek saath band hongi?'",
                            "Distinguishing short-term price fluctuation from permanent business death",
                            "Verbatim Hinglish reassurance script for conservative parents"
                        ],
                        "know": "Mutual funds are institutional trusts holding registered securities under SEBI and custodian oversight.",
                        "understand": "You must never dismiss the fear; you must validate it and replace hearsay with institutional facts.",
                        "do": "Record a 60-second video response using the Turtlemint Objection Script.",
                        "say": "\"Sharma ji, aapka darr bilkul natural hai. Par yeh koi chit fund nahi hai—yeh desh ki top 50 companiyon mein hissa hai.\"",
                        "never_claim": "NEVER SAY: 'Mutual fund mein bilkul koi risk nahi hota, paisa kabhi doob hi nahi sakta.'"
                    },
                    {
                        "lesson_id": "L15.02",
                        "title": "Dialogue 2: 'Bank FD 7.5% Guaranteed De Raha Hai, MF Kyun Loon?'",
                        "topic": "Reframing the Fixed Deposit Safe Haven",
                        "format": "Visual Math Comparison Infographic",
                        "duration": "13 mins",
                        "subtopics": [
                            "Respecting the FD: Acknowledging that FDs are great for safety and short-term capital preservation",
                            "The Treadmill Math: Showing the net in-hand return of a 7.5% FD after 30% tax bracket (Net 5.25%)",
                            "The Inflation Reality: If inflation is 6% and net FD return is 5.25%, the real return is -0.75%",
                            "The 10-Year Wealth Gap: Comparing ₹10 Lakh in FD vs a Balanced Advantage / Equity fund over 10 years",
                            "The Peaceful Blend: Pitching a combination of FD for immediate safety + MF for wealth creation"
                        ],
                        "know": "FD interest is taxed annually at slab rates, severely reducing post-tax compounding for taxpayers.",
                        "understand": "The goal is not to kill the FD, but to show that an FD alone cannot fund long-term retirement or education goals.",
                        "do": "Run the FD vs Equity Post-Tax Compounding Calculator on Turtlemint Ninja.",
                        "say": "\"FD short-term safety ke liye behtareen hai, par 10 saal ke sapno ke liye FD mehangai se haar jaati hai.\"",
                        "never_claim": "Never claim that mutual funds replace bank FDs for 6-month or 1-year goals."
                    },
                    {
                        "lesson_id": "L15.03",
                        "title": "Dialogue 3: 'Market Gir Raha Hai, Meri SIP Pause Kar Do!'",
                        "topic": "De-escalating Customer Panic During Crashes",
                        "format": "WhatsApp Voice Note Template + Roleplay",
                        "duration": "15 mins",
                        "subtopics": [
                            "The First 15 Seconds: Emotional de-escalation ('I understand why you are worried, and I am here with you')",
                            "The Festive Shopping Analogy: 'Diwali sale pe jab 40% discount milta hai, tab hum shopping band karte hain kya?'",
                            "The Mathematical Reality: Showing how today's ₹5,000 is buying 30% more units than 4 months ago",
                            "The Historical Proof: Showing how investors who continued SIPs in 2008 and 2020 became wealthy",
                            "The Golden Action: Asking the client to commit to waiting just 6 months before making any hasty decision"
                        ],
                        "know": "Stopping an SIP during a market crash permanently locks in lower returns and eliminates rupee-cost averaging.",
                        "understand": "When a customer calls in panic, they do not want technical data; they want emotional reassurance and leadership.",
                        "do": "Send a pre-approved Turtlemint reassurance graphic to a panicking client.",
                        "say": "\"Aapki SIP koi kharcha nahi hai—aaj market gira hai, matlab wahi shares discount par mil rahe hain!\"",
                        "never_claim": "Never promise that the market will bounce back next week or that the crash is officially over."
                    },
                    {
                        "lesson_id": "L15.04",
                        "title": "Dialogue 4: 'Past Mein 25% Diya Hai, Future Mein Bhi Dega na?'",
                        "topic": "Anchoring Unrealistic Customer Expectations",
                        "format": "Rubber Band Mean Reversion Animation",
                        "duration": "12 mins",
                        "subtopics": [
                            "The Rubber Band Analogy: What stretches too far in one direction must contract back to its historical mean",
                            "Understanding Market Cycles: After a 30% rally year, moderate 8-12% years or temporary corrections are normal",
                            "The Danger of Return Anchoring: Why assuming 25% returns leads clients to under-invest for their goals",
                            "Setting the Baseline: Recommending conservative 11-13% long-term expectations for equity planning",
                            "The Mandatory SEBI Truth: 'Past performance may or may not be sustained in the future'"
                        ],
                        "know": "Equities experience mean reversion; exceptionally high 1-year returns are almost never sustained consecutively.",
                        "understand": "Conservative goal projections protect the DP from future customer disappointment and churn.",
                        "do": "Adjust a goal plan on Turtlemint Ninja from an aggressive 18% assumption down to a realistic 12% assumption.",
                        "say": "\"Pichla saal extraordinary tha, par planning ke liye hum 11-12% ka realistic return maan kar chalenge.\"",
                        "never_claim": "Never imply or promise that past high returns will continue into the future."
                    }
                ]
            }
        ]
    },

    # LEVEL 16
    {
        "level_num": 16,
        "level_title": "Mis-Selling, Compliance & Ethical Distribution",
        "level_tagline": "The Iron Guardrails: SEBI Regulations, AMFI Code of Conduct & Distributor Boundaries",
        "phase": "Phase 5: Field Mastery — Customer Discovery, Pitch & Compliance",
        "modules": [
            {
                "module_id": "M16.1",
                "module_title": "Statutory Prohibitions & Professional Ethics",
                "lessons": [
                    {
                        "lesson_id": "L16.01",
                        "title": "The Red Lines: Absolute Regulatory Prohibitions",
                        "topic": "The Non-Negotiables of Distribution",
                        "format": "Courtroom Dramatization Video + Penalty Cards",
                        "duration": "15 mins",
                        "subtopics": [
                            "Prohibition 1: Promising or implying any guaranteed, assured, or fixed returns (SEBI MF Reg 1996)",
                            "Prohibition 2: Handling physical cash or taking client cheques in your own personal name",
                            "Prohibition 3: Rebating or passing back distribution commissions to induce clients to buy",
                            "Prohibition 4: Taking pre-signed blank forms or entering client transaction OTPs on your own device",
                            "Consequences of Violations: Immediate termination of ARN, forfeiture of trail commissions, SEBI legal action"
                        ],
                        "know": "Promising guaranteed returns or sharing commissions with investors leads to permanent debarment by AMFI/SEBI.",
                        "understand": "A single compliance violation destroys your entire career, your reputation, and your lifetime compounding trail income.",
                        "do": "Review and digitally sign the Turtlemint Annual Compliance Undertaking.",
                        "say": "\"SEBI ke sakht niyam hain—koi bhi distributor return guarantee nahi kar sakta, aur hum 100% compliant kaam karte hain.\"",
                        "never_claim": "NEVER violate any of the four absolute red lines under any circumstance or customer pressure."
                    },
                    {
                        "lesson_id": "L16.02",
                        "title": "Distributor (MFD) vs. Investment Adviser (RIA): Boundaries & Disclosures",
                        "topic": "Legal Boundaries of Financial Intermediation",
                        "format": "Two-Column Operational Guide",
                        "duration": "13 mins",
                        "subtopics": [
                            "What is an AMFI-Registered Mutual Fund Distributor (MFD)? An intermediary distributing regular plans",
                            "What is a SEBI Registered Investment Adviser (RIA)? A fee-charging fiduciary providing independent advice",
                            "Can an MFD charge 'advisory fees'? NO! Distributors earn commission from the AMC; charging advice fees is illegal",
                            "The Incidental Advice Rule: Providing product suitability and goal mapping incidental to distribution",
                            "Commission Disclosure Norms: Providing full transparency of AMC trailing commission structures"
                        ],
                        "know": "Distributors cannot charge advisory fees or use the title 'Financial Adviser' unless registered under SEBI RIA regulations.",
                        "understand": "Positioning yourself truthfully as an execution and servicing partner builds far greater long-term trust.",
                        "do": "Verify that all customer emails and business cards state 'AMFI Registered Mutual Fund Distributor Partner'.",
                        "say": "\"Main ek AMFI-registered mutual fund partner hoon—main aapko sahi product choose karne aur service dene mein madad karta hoon.\"",
                        "never_claim": "Never call yourself an 'Independent Financial Adviser (IFA)' or charge consulting fees to a client."
                    }
                ]
            }
        ]
    }
]
