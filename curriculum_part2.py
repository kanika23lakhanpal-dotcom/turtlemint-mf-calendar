# -*- coding: utf-8 -*-
# Levels 6 to 11

LEVELS_6_TO_11 = [
    # LEVEL 6
    {
        "level_num": 6,
        "level_title": "Understanding Risk",
        "level_tagline": "Beyond Marketing Pamphlets: Volatility, Defaults & The Riskometer",
        "phase": "Phase 3: The Diagnostic Eye — Risk, Returns & Factsheets",
        "modules": [
            {
                "module_id": "M06.1",
                "module_title": "Deconstructing Real Risk vs. Volatility",
                "lessons": [
                    {
                        "lesson_id": "L06.01",
                        "title": "Risk vs. Volatility: The Ocean Wave Analogy",
                        "topic": "Fluctuation vs Permanent Capital Loss",
                        "format": "Ocean Ferry Explainer Animation",
                        "duration": "12 mins",
                        "subtopics": [
                            "What is Volatility? Daily price movements caused by news, sentiment, and liquidity fluctuations",
                            "What is Real Risk? The permanent destruction of invested capital (insolvency, fraud, permanent shutdown)",
                            "The Ferry Analogy: Ocean waves rocking the boat (Volatility) vs the boat having a hole in the bottom (Real Risk)",
                            "Why daily volatility is the price of admission for long-term equity compounding",
                            "The time horizon cure: How extending holding period compresses downside volatility toward zero"
                        ],
                        "know": "Volatility is price noise over days and months; true risk is permanent loss of capital.",
                        "understand": "Checking portfolio NAV every single morning creates artificial panic and tricks investors into exiting sound businesses.",
                        "do": "Show rolling 7-year return distributions of Nifty 50 showing zero negative return periods historically.",
                        "say": "\"Utaar-chadhao (volatility) ek lehar jaisi hai, boat doob nahi rahi hai—safar poora hone dijiye.\"",
                        "never_claim": "Never dismiss a customer's genuine fear of volatility; empathize first before explaining the math."
                    },
                    {
                        "lesson_id": "L06.02",
                        "title": "The Three Horsemen of Debt Risk: Credit, Interest Rate & Liquidity",
                        "topic": "How Fixed Income Instruments Lose Money",
                        "format": "Interactive Debt Risk Seesaw",
                        "duration": "14 mins",
                        "subtopics": [
                            "Credit Risk (Default Risk): When a corporate borrower fails to pay interest or repay principal",
                            "The Credit Rating Scale: AAA (Safest), AA, A, BBB down to D (Default) and write-downs",
                            "Interest Rate Risk & Duration: Why bond prices fall when RBI raises interest rates (The Seesaw Rule)",
                            "Modified Duration: If duration is 5 years and interest rates rise 1%, NAV drops ~5%",
                            "Liquidity Risk: Inability of a debt fund manager to sell illiquid corporate bonds during heavy redemptions"
                        ],
                        "know": "When market interest rates go up, existing bond prices go down, hurting long-duration debt funds.",
                        "understand": "Debt funds are not zero-risk alternatives to bank FDs; conservative clients belong in short-duration AAA/Sovereign funds.",
                        "do": "Check the average maturity and credit rating breakdown of a debt scheme on Turtlemint Pro.",
                        "say": "\"Debt fund mein bhi risk hota hai—agar byaj dar badhti hai ya company default karti hai, toh NAV gir sakti hai.\"",
                        "never_claim": "Never describe debt funds as 'guaranteed like government bonds' unless referring strictly to pure G-Sec schemes held to maturity."
                    },
                    {
                        "lesson_id": "L06.03",
                        "title": "Concentration, Sector & Reinvestment Risks",
                        "topic": "Portfolio Specific Vulnerabilities",
                        "format": "Visual Vulnerability Grid",
                        "duration": "10 mins",
                        "subtopics": [
                            "Concentration Risk: Holding too much of a single stock (e.g., >10% in one company)",
                            "Sector Risk: Over-exposure to one segment of the economy (e.g., 40% in banking or IT)",
                            "Reinvestment Risk: Being forced to reinvest maturing money at lower prevailing interest rates",
                            "Currency & Geopolitical Risk: What happens when investing in international mutual funds",
                            "How broad-market diversification acts as the ultimate antidote to single-company disasters"
                        ],
                        "know": "Diversification across 40-50 stocks eliminates unsystematic (company-specific) risk entirely.",
                        "understand": "A fund with 15 stocks carries vastly higher vulnerability than a fund with 60 stocks across 10 sectors.",
                        "do": "Inspect the Top 10 stock concentration percentage in a client's selected scheme.",
                        "say": "\"Diversification ka matlab hai ki ek company ke kharab performance se aapka poora portfolio barbaad na ho.\"",
                        "never_claim": "Never claim that diversification eliminates systemic broad-market crash risks."
                    }
                ]
            },
            {
                "module_id": "M06.2",
                "module_title": "Measuring & Categorizing Risk",
                "lessons": [
                    {
                        "lesson_id": "L06.04",
                        "title": "Decoding the SEBI Riskometer: The 6 Levels",
                        "topic": "Standardized Scheme Risk Labeling",
                        "format": "Interactive Riskometer Gauge",
                        "duration": "11 mins",
                        "subtopics": [
                            "The 6-tier Riskometer: Low, Low to Moderate, Moderate, Moderately High, High, Very High",
                            "How AMCs calculate Riskometer scores based on monthly portfolio composition",
                            "Debt score drivers: Liquidity score, interest rate score, and credit risk score",
                            "Equity score drivers: Market capitalization, volatility, and impact cost",
                            "Mandatory disclosure: Why the Riskometer must appear in every product fact sheet and customer proposal"
                        ],
                        "know": "Riskometer ratings are updated every month based on actual securities held in the portfolio.",
                        "understand": "The Riskometer provides an immediate, standardized red flag if a scheme's risk exceeds a client's profile.",
                        "do": "Show a customer where the Riskometer gauge is displayed on Turtlemint Ninja scheme pages.",
                        "say": "\"Riskometer car ke speedometer jaisa hai—yeh batata hai ki yeh scheme kitni tez chal rahi hai aur kitna jhatka de sakti hai.\"",
                        "never_claim": "Never present a 'Very High' risk equity scheme to a client as a 'moderate risk' product."
                    },
                    {
                        "lesson_id": "L06.05",
                        "title": "Risk Appetite vs. Risk Capacity: The Critical Distinction",
                        "topic": "Psychological Willingness vs Financial Reality",
                        "format": "Case Scenario Analysis Cards",
                        "duration": "12 mins",
                        "subtopics": [
                            "What is Risk Appetite? The emotional and psychological willingness to tolerate portfolio drops",
                            "What is Risk Capacity? The mathematical and financial ability to absorb losses without personal disaster",
                            "The Rope Bridge Analogy: A brave hiker (High Appetite) with a broken leg (Zero Capacity) cannot cross",
                            "Mismatches: The young freelancer with volatile income vs the retired civil servant with an assured pension",
                            "The Suitability Rule: Why the investment plan must ALWAYS be anchored to the LOWER of the two"
                        ],
                        "know": "Risk capacity is determined by age, dependents, job stability, emergency fund, and goal horizon.",
                        "understand": "An aggressive 25-year-old with 5 dependents and zero emergency savings has LOW risk capacity despite high appetite.",
                        "do": "Complete the 5-question Turtlemint Risk Capacity Profiler before recommending any equity scheme.",
                        "say": "\"Aap dil se kitna risk le sakte hain (appetite) aur aapka bank balance kitna jhel sakta hai (capacity)—hume dono dekhna hai.\"",
                        "never_claim": "Never let an aggressive client invest money needed in 6 months into high-risk equity funds."
                    }
                ]
            }
        ]
    },

    # LEVEL 7
    {
        "level_num": 7,
        "level_title": "Understanding Returns",
        "level_tagline": "The Truth Behind Metrics: Absolute, CAGR, XIRR & Rolling Returns",
        "phase": "Phase 3: The Diagnostic Eye — Risk, Returns & Factsheets",
        "modules": [
            {
                "module_id": "M07.1",
                "module_title": "The Mathematical Foundations of Return",
                "lessons": [
                    {
                        "lesson_id": "L07.01",
                        "title": "Absolute Return vs. CAGR: Why Time Changes Everything",
                        "topic": "Point-to-Point vs Annualized Compounding",
                        "format": "Interactive Calculation Tool + Visual Proof",
                        "duration": "13 mins",
                        "subtopics": [
                            "Absolute Return: (Final Value - Initial Value) ÷ Initial Value × 100 (Only valid for <1 year)",
                            "Why quoting '60% return' over 5 years is misleading: It equates to only ~9.8% annualized",
                            "Compound Annual Growth Rate (CAGR): The smoothed annual growth rate of a lump-sum investment",
                            "The CAGR Formula: CAGR = (Final Value / Initial Value)^(1 / Years) - 1",
                            "The Rule: Absolute for periods under 1 year, CAGR for lump sum periods exceeding 1 year"
                        ],
                        "know": "Absolute return ignores the time taken to generate the profit; CAGR normalizes return to a per-year basis.",
                        "understand": "A fund giving 100% return over 10 years sounds incredible, but is only a modest 7.2% CAGR.",
                        "do": "Convert a client's 3-year absolute return into annualized CAGR on Turtlemint Ninja.",
                        "say": "\"Aapka paisa 3 saal mein 50% badha, iska matlab har saal lagbhag 14.5% ki speed se badha hai.\"",
                        "never_claim": "Never market multi-year returns using simple absolute percentages without clearly displaying CAGR."
                    },
                    {
                        "lesson_id": "L07.02",
                        "title": "XIRR: The Only Honest Metric for SIP Returns",
                        "topic": "Extended Internal Rate of Return",
                        "format": "Dynamic Cash Flow Timeline Simulator",
                        "duration": "15 mins",
                        "subtopics": [
                            "Why CAGR fails completely for SIPs: Each installment has a different investment date and holding period",
                            "Installment 1 has been invested for 36 months; Installment 36 has been invested for only 30 days!",
                            "What is XIRR? The internal rate of return that equates all past cash inflows and current portfolio value",
                            "Why a fund's published 1-year CAGR can be +25% while the client's 1-year SIP XIRR is +14%",
                            "Interpreting the Turtlemint statement: Teaching clients where to find and read their true XIRR"
                        ],
                        "know": "XIRR is the only mathematically correct return metric for periodic or irregular investments like SIPs.",
                        "understand": "In the early months of an SIP, XIRR numbers fluctuate wildly because late installments have had zero time to compound.",
                        "do": "Calculate live XIRR for a 12-month recurring SIP statement using Turtlemint Ninja.",
                        "say": "\"XIRR aapke har ek SIP installment ke alag-alag time period ko count karke ek accurate annual return nikaalta hai.\"",
                        "never_claim": "Never tell a customer that their SIP return will match the scheme's 1-year published CAGR."
                    }
                ]
            },
            {
                "module_id": "M07.2",
                "module_title": "Benchmarks, Indices & Performance Integrity",
                "lessons": [
                    {
                        "lesson_id": "L07.03",
                        "title": "Benchmarks & The Total Return Index (TRI)",
                        "topic": "Measuring True Value-Add",
                        "format": "Pace Car Marathon Video",
                        "duration": "12 mins",
                        "subtopics": [
                            "What is a Benchmark? The standard reference yardstick (e.g., Nifty 50, BSE 500, CRISIL Composite)",
                            "The Marathon Analogy: Running at 10 km/h is meaningless if the pace car is running at 14 km/h",
                            "Price Return Index (PRI) vs. Total Return Index (TRI): The dividend inclusion revolution",
                            "Why SEBI mandated TRI: Preventing AMCs from comparing stock price gains against dividend-reinvested funds",
                            "Alpha: The excess return generated by an active fund manager over and above the benchmark TRI"
                        ],
                        "know": "Under SEBI rules, all mutual fund performance must be benchmarked against the Total Return Index (TRI).",
                        "understand": "If a fund generates 15% return while its benchmark TRI generates 18%, the fund manager destroyed value (negative alpha).",
                        "do": "Compare an equity fund's 5-year return against its mandatory benchmark TRI on Turtlemint Pro.",
                        "say": "\"Fund ka return dekhna kaafi nahi hai—yeh dekhna zaroori hai ki usne apne benchmark ko beat kiya ya nahi.\"",
                        "never_claim": "Never compare an active equity fund to an outdated Price Return Index (PRI) to artificially inflate performance."
                    },
                    {
                        "lesson_id": "L07.04",
                        "title": "The Deception of Trailing Returns vs. The Truth of Rolling Returns",
                        "topic": "Eliminating Point-to-Point Bias",
                        "format": "Rolling Window Interactive Chart",
                        "duration": "14 mins",
                        "subtopics": [
                            "What are Trailing Returns? Point-to-point returns (1-year, 3-year, 5-year) anchored to today's date",
                            "The Endpoint Bias Trap: Why a sharp market rally yesterday can make a mediocre 3-year fund look like a superstar",
                            "What are Rolling Returns? Calculating hundreds of 3-year or 5-year holding periods on every single calendar day",
                            "Measuring Consistency: What percentage of time did the fund beat the benchmark across rolling periods?",
                            "Downside Protection: How did the fund perform during rolling periods when the broader market was negative?"
                        ],
                        "know": "Rolling returns eliminate point-to-point starting and ending date bias, revealing true manager consistency.",
                        "understand": "A fund with modest trailing returns might actually be far more consistent and reliable on rolling metrics.",
                        "do": "Look up the 5-year rolling return distribution of two competing funds on Turtlemint Pro.",
                        "say": "\"Trailing return ek match ka score hai, rolling return poore tournament ka batting average hai.\"",
                        "never_claim": "Never recommend a mutual fund based purely on its 1-year trailing return leaderboard ranking."
                    }
                ]
            }
        ]
    },

    # LEVEL 8
    {
        "level_num": 8,
        "level_title": "How to Read a Mutual Fund Factsheet",
        "level_tagline": "The Diagnostic X-Ray: Deciphering Portfolio Holdings, Costs & Risk Metrics",
        "phase": "Phase 3: The Diagnostic Eye — Risk, Returns & Factsheets",
        "modules": [
            {
                "module_id": "M08.1",
                "module_title": "Factsheet Anatomy & Portfolio Diagnostics",
                "lessons": [
                    {
                        "lesson_id": "L08.01",
                        "title": "The 5-Minute Factsheet Navigation Framework",
                        "topic": "Extracting Vital Signs from AMC Disclosures",
                        "format": "Interactive Annotated Factsheet Explorer",
                        "duration": "15 mins",
                        "subtopics": [
                            "Where to find factsheets: Monthly publication on AMC websites and Turtlemint Pro document libraries",
                            "The 5 vital signs: Inception Date, AUM, Benchmark, Expense Ratio, and Current Riskometer",
                            "Reading the Investment Objective: What the scheme legally promises to do (and not do)",
                            "Top 10 Holdings: What percentage of total capital is concentrated in the top 10 stocks?",
                            "Sector Allocation Breakdown: Checking if the fund manager is making outsized sector bets"
                        ],
                        "know": "Factsheets are published monthly by every AMC under mandatory SEBI transparency rules.",
                        "understand": "Reading a factsheet is like reading a medical blood report; 5 key metrics reveal the entire health of the fund.",
                        "do": "Complete a 3-minute factsheet scavenger hunt on Turtlemint Pro: Find Top 3 holdings, AUM, and TER of a live fund.",
                        "say": "\"Factsheet mutual fund ka X-ray report hai—yeh batata hai ki aapka ek-ek rupaya kahan invest hua hai.\"",
                        "never_claim": "Never assume factsheet data from 6 months ago is current; always verify the latest month-end edition."
                    },
                    {
                        "lesson_id": "L08.02",
                        "title": "Portfolio Turnover Ratio (PTR) & Cash Holdings",
                        "topic": "Evaluating Churn and Liquidity Drag",
                        "format": "Traffic Lane Churn Analogy Video",
                        "duration": "11 mins",
                        "subtopics": [
                            "What is Portfolio Turnover Ratio? The percentage of a fund's holdings that have changed over the past year",
                            "High PTR (>100%): Hyperactive trading, higher brokerage friction, momentum-driven strategy",
                            "Low PTR (<30%): Buy-and-hold high-conviction philosophy, lower transaction drag",
                            "Understanding Cash Holdings: Why equity funds hold 2% to 7% in cash or reverse repos",
                            "Cash as an active manager call: Preparing for bargains vs missing out on market rallies (Cash Drag)"
                        ],
                        "know": "High portfolio turnover generates transaction costs and stamp duty inside the scheme, impacting net returns.",
                        "understand": "A fund holding 15% cash in a roaring bull market will lag its benchmark due to cash drag.",
                        "do": "Identify the PTR and cash percentage on a sample equity scheme factsheet.",
                        "say": "\"Turnover ratio batata hai ki manager stocks jaldi-jaldi badal raha hai ya lambe samay ke liye hold kar raha hai.\"",
                        "never_claim": "Never label high turnover as automatically bad; some momentum strategies thrive on high turnover."
                    }
                ]
            },
            {
                "module_id": "M08.2",
                "module_title": "Statistical Metrics: Standard Deviation, Beta & Sharpe",
                "lessons": [
                    {
                        "lesson_id": "L08.03",
                        "title": "Volatility Metrics: Standard Deviation & Beta",
                        "topic": "Quantifying Dispersion & Market Sensitivity",
                        "format": "Highway Driving Speed Visualizer",
                        "duration": "14 mins",
                        "subtopics": [
                            "What is Standard Deviation (SD)? The measure of how wildly a fund's monthly returns swing around its average",
                            "The Highway Analogy: Cruising steadily at 80 km/h (Low SD) vs swinging between 30 km/h and 150 km/h (High SD)",
                            "What is Beta? The sensitivity of the fund's price movements relative to its benchmark",
                            "Beta = 1.0 (Moves exactly in tandem with market); Beta = 1.3 (30% more aggressive); Beta = 0.8 (20% more defensive)",
                            "How conservative investors benefit from low-Beta, low-SD funds for a smoother emotional journey"
                        ],
                        "know": "Standard Deviation measures total volatility; Beta measures relative market sensitivity.",
                        "understand": "A high-Beta fund will surge higher in a bull market, but crash far harder during corrections.",
                        "do": "Compare the Beta of a Large Cap fund (e.g., 0.85) with a Small Cap fund (e.g., 1.25) on Turtlemint Pro.",
                        "say": "\"Beta batata hai ki jab market 10% girega, toh yeh fund 8% girega ya 13%.\"",
                        "never_claim": "Never use complex Greek statistical terms in customer meetings without immediately translating them into vehicle analogies."
                    },
                    {
                        "lesson_id": "L08.04",
                        "title": "Risk-Adjusted Ratios: Sharpe & Sortino Ratios",
                        "topic": "Measuring Return Per Unit of Risk Taken",
                        "format": "Stunt Driver vs Chauffeur Comparison",
                        "duration": "13 mins",
                        "subtopics": [
                            "The Core Question: Did the fund manager generate returns through brilliant skill or reckless risk?",
                            "The Risk-Free Rate (Rf): The baseline yield of 91-day Treasury Bills that anyone could get without risk",
                            "Sharpe Ratio: (Fund Return - Risk Free Rate) ÷ Standard Deviation (Reward per unit of total risk)",
                            "Sortino Ratio: Penalizes ONLY downside volatility, ignoring joyful upside spikes",
                            "Why a fund with 14% return and a 1.2 Sharpe Ratio is far superior to a fund with 16% return and a 0.6 Sharpe Ratio"
                        ],
                        "know": "A higher Sharpe or Sortino ratio indicates superior risk-adjusted performance.",
                        "understand": "Chasing the highest raw return without checking Sharpe ratio leads investors into dangerously volatile portfolios.",
                        "do": "Rank 5 funds in the same category by Sharpe ratio using the Turtlemint scheme comparison screener.",
                        "say": "\"Sharpe ratio batata hai ki manager ne return kamane ke liye kitna khatra uthaya—jitna zyada, utna behtar.\"",
                        "never_claim": "Never compare Sharpe ratios across different categories (e.g., comparing Large Cap Sharpe to Debt Fund Sharpe)."
                    }
                ]
            }
        ]
    },

    # LEVEL 9
    {
        "level_num": 9,
        "level_title": "How to Compare Mutual Funds",
        "level_tagline": "Apples to Apples: Category Discipline, Downside Capture & Manager Tenure",
        "phase": "Phase 3: The Diagnostic Eye — Risk, Returns & Factsheets",
        "modules": [
            {
                "module_id": "M09.1",
                "module_title": "Category Discipline & The Peer Group",
                "lessons": [
                    {
                        "lesson_id": "L09.01",
                        "title": "The Cardinal Rule: Apples to Apples Only",
                        "topic": "Preventing Cross-Category Distortion",
                        "format": "Fruit Basket Analogy Infographic",
                        "duration": "11 mins",
                        "subtopics": [
                            "Why comparing a Small Cap fund's return to a Large Cap fund is fundamentally fraudulent",
                            "Comparing a motorcycle to a 10-ton truck: Different engines, different roads, different cargo",
                            "The Category Benchmark: Comparing a scheme against its peer group median and category average",
                            "Understanding quartile rankings: Quartile 1 (Top 25%) vs Quartile 4 (Bottom 25%) consistency",
                            "Why yesterday's top quartile fund frequently drops to quartile 4 due to style rotation"
                        ],
                        "know": "Schemes must strictly be evaluated against peers operating under the exact same SEBI category mandate.",
                        "understand": "A customer asking 'Which fund gave 30%?' must be educated on why category mandates dictate risk limits.",
                        "do": "Spot the invalid comparison in a sample customer-created mutual fund watchlist.",
                        "say": "\"Hum kabhi cricket batsman ki tulna football striker se nahi kar sakte—dono ke rules alag hain.\"",
                        "never_claim": "Never compare a hybrid fund's performance against a pure equity index to make the hybrid look 'safe and high returning'."
                    },
                    {
                        "lesson_id": "L09.02",
                        "title": "Downside Capture vs. Upside Capture Ratio",
                        "topic": "How the Fund Behaves in Bull vs Bear Cycles",
                        "format": "Dual-Shield Interactive Graphic",
                        "duration": "12 mins",
                        "subtopics": [
                            "What is Upside Capture Ratio? Percentage of benchmark gains captured when the market is rising (>100% is great)",
                            "What is Downside Capture Ratio? Percentage of benchmark losses suffered when the market is falling (<100% is stellar)",
                            "The Holy Grail of Long-Term Wealth: Capturing 90% of the upside while suffering only 60% of the downside",
                            "The Math of Recovery: If you lose 50%, you need a 100% gain just to get back to zero!",
                            "Why funds that protect capital during crashes compound far faster over 15-year cycles"
                        ],
                        "know": "A downside capture ratio below 100% indicates the fund fell less than its benchmark during market drops.",
                        "understand": "Preserving capital during bear markets is mathematically more important for long-term compounding than shooting lights out in bull runs.",
                        "do": "Inspect the Upside/Downside capture ratios of two competing Flexi Cap funds on Turtlemint Pro.",
                        "say": "\"Asli champion fund woh hai jo girte bazaar mein kam gire—kyunki recovery mein usko kam mehnat karni padti hai.\"",
                        "never_claim": "Never promise that a fund with low downside capture will never show negative monthly returns."
                    }
                ]
            },
            {
                "module_id": "M09.2",
                "module_title": "Fund Manager Tenure & AMC Pedigree",
                "lessons": [
                    {
                        "lesson_id": "L09.03",
                        "title": "Evaluating the Fund Manager & Process vs. Star Culture",
                        "topic": "Key-Man Risk & Institutional Rigor",
                        "format": "Football Club Analogy Explainer",
                        "duration": "11 mins",
                        "subtopics": [
                            "Manager Tenure: How long has the current fund manager been running this specific scheme?",
                            "The Track Record Dilemma: Did the 10-year track record belong to the current manager or someone who left last year?",
                            "Process-Driven AMCs vs Star Manager-Driven AMCs: Why institutional investment committees matter",
                            "Key-Man Risk: What should a DP do when a famous fund manager resigns? (Wait and evaluate, don't panic-churn)",
                            "Evaluating the AMC's overall lineage, risk management culture, and debt compliance history"
                        ],
                        "know": "A 10-year fund track record is irrelevant if the current manager took over only 6 months ago.",
                        "understand": "AMCs with robust, repeatable processes survive manager exits without long-term damage to investor wealth.",
                        "do": "Check the fund manager tenure and other schemes managed by the same person on Turtlemint Pro.",
                        "say": "\"Hum individual star manager ke peeche nahi bhaagte, AMC ke solid investment process par bharosa karte hain.\"",
                        "never_claim": "Never urge a client to redeem their entire portfolio immediately just because a fund manager resigned."
                    }
                ]
            }
        ]
    },

    # LEVEL 10
    {
        "level_num": 10,
        "level_title": "Goal-Based Investing",
        "level_tagline": "Moving from Random Products to Life Milestones: Time Horizon Architecture",
        "phase": "Phase 4: Goal Advisory, Tax & Costs",
        "modules": [
            {
                "module_id": "M10.1",
                "module_title": "The Goal Architecture & Time Horizon Mapping",
                "lessons": [
                    {
                        "lesson_id": "L10.01",
                        "title": "The Multi-Jar Framework: Categorizing Family Goals",
                        "topic": "Purpose-Driven Financial Planning",
                        "format": "Interactive Family Mason Jar Visualizer",
                        "duration": "14 mins",
                        "subtopics": [
                            "Why product-first selling fails: 'Kaunsa fund best hai?' is the wrong question to answer",
                            "The correct question: 'Paisa kis kaam ke liye aur kitne saal baad chahiye?'",
                            "Bucket 1 - Emergency Fund: 6 months of household expenses in Liquid/Overnight funds (Immediate safety)",
                            "Bucket 2 - Short-Term Goals (<3 years): Car downpayment, vacation, home renovation (Zero equity)",
                            "Bucket 3 - Medium-Term Goals (3-5 years): Higher secondary school, business seed capital (Hybrid/BAF)",
                            "Bucket 4 - Long-Term Goals (7-15+ years): Child's college degree, daughter's wedding, retirement (Pure Equity)"
                        ],
                        "know": "The investment time horizon dictates the asset class; never match short-term goals with volatile equity.",
                        "understand": "When money has a clear family purpose (Pari ki Padhai), the client will not stop their SIP during market crashes.",
                        "do": "Map a customer's life goals into 4 visual buckets using the Turtlemint Ninja Goal Mapper.",
                        "say": "\"Pehle decide karte hain ki yeh paisa kis sapne ke liye hai—product toh baad mein apne aap decide ho jayega.\"",
                        "never_claim": "Never allocate money needed within 3 years into mid-cap or small-cap equity funds."
                    },
                    {
                        "lesson_id": "L10.02",
                        "title": "Sizing Future Goals: Factoring in Education & Medical Inflation",
                        "topic": "Mathematical Goal Quantification",
                        "format": "Dynamic Future Value Calculator",
                        "duration": "13 mins",
                        "subtopics": [
                            "The Future Value Formula: FV = PV × (1 + r)^n made simple through interactive software",
                            "Why general CPI inflation (6%) fails for education: Education inflation runs at 10-12% annually in India",
                            "The ₹25 Lakh Reality: A medical or engineering degree costing ₹8 Lakh today will cost ₹25 Lakh in 12 years",
                            "Sizing the Retirement Corpus: The 25x-30x annual expense rule for dignified retirement",
                            "Calculating the exact monthly SIP required to achieve the inflation-adjusted target"
                        ],
                        "know": "Failing to account for 10% education inflation leaves parents with a 50% funding deficit when college starts.",
                        "understand": "Showing parents the real future cost of a college degree creates immediate, urgent clarity on the need for equity SIPs.",
                        "do": "Calculate the exact future cost of an ₹8 Lakh course in 14 years at 10% inflation on Turtlemint Ninja.",
                        "say": "\"Agar hum aaj sirf ₹8 Lakh ka plan banayenge, toh 12 saal baad aadha paisa kam pad jayega.\"",
                        "never_claim": "Never guarantee that a calculated SIP will hit the target with 100% precision; review annually."
                    },
                    {
                        "lesson_id": "L10.03",
                        "title": "The De-Risking Flight Path: Protecting Goals Near Maturity",
                        "topic": "Systematic Glide-Paths to Safety",
                        "format": "Aircraft Landing Analogy Animation",
                        "duration": "12 mins",
                        "subtopics": [
                            "The Airplane Landing Analogy: You don't cut the engine at 30,000 feet; you begin descent 30 minutes early",
                            "What happens if an equity market crashes 30% two months before your child's college admission fee is due?",
                            "The Systematic De-risking Plan: Activating an STP from Equity to Debt 2-3 years before goal deadline",
                            "Moving from 80% equity at Year 10 $\rightarrow$ 50% at Year 12 $\rightarrow$ 10% at Year 14 $\rightarrow$ 100% Liquid at Year 15",
                            "Protecting locked-in accumulated gains from last-minute market volatility"
                        ],
                        "know": "Portfolios must be systematically shifted from volatile equity to capital-preserving debt 2-3 years before goal maturity.",
                        "understand": "Accumulating wealth requires taking calculated risk; preserving accumulated wealth requires eliminating risk on time.",
                        "do": "Set up a calendar trigger for a client whose goal is 36 months away to begin systematic de-risking.",
                        "say": "\"Goal ke aakhri 2 saal mein hum saara profit equity se nikaal kar safe debt fund mein daal dete hain taaki koi risk na rahe.\"",
                        "never_claim": "Never advise a client to stay 100% invested in equity up until the final week before money is required."
                    }
                ]
            }
        ]
    },

    # LEVEL 11
    {
        "level_num": 11,
        "level_title": "Asset Allocation",
        "level_tagline": "The Only Free Lunch in Finance: Diversification, Correlation & Rebalancing",
        "phase": "Phase 4: Goal Advisory, Tax & Costs",
        "modules": [
            {
                "module_id": "M11.1",
                "module_title": "The Power of Asset Allocation",
                "lessons": [
                    {
                        "lesson_id": "L11.01",
                        "title": "The Balanced Thali: Why Asset Allocation Drives 90% of Returns",
                        "topic": "The Science of Portfolio Construction",
                        "format": "Indian Thali Nutrition Analogy",
                        "duration": "13 mins",
                        "subtopics": [
                            "The Academic Truth: Studies prove asset allocation explains >90% of portfolio return variability, not stock picking",
                            "The Balanced Diet Thali: Rice/Roti (Core Equity), Dal/Sabzi (Stable Debt), Pickle/Salad (Gold/Liquid)",
                            "Negative and Low Correlation: Why Gold and Debt cushion the fall when Equity markets correct",
                            "The Three Classic Profiles: Conservative (25:75 Equity:Debt), Moderate (50:50), Aggressive (70:30)",
                            "Why one single mutual fund scheme can never solve every family financial need"
                        ],
                        "know": "Asset allocation is the proportion of total wealth distributed across distinct asset classes.",
                        "understand": "No single asset class wins every year; a diversified portfolio guarantees you always hold this year's winner.",
                        "do": "Use Turtlemint Pro's Asset Allocation Wheel to build a customized 60:30:10 Equity:Debt:Gold portfolio.",
                        "say": "\"Jaise thali mein sirf mirchi ya sirf meetha nahi hota, waise hi portfolio mein equity aur debt dono chahiye.\"",
                        "never_claim": "Never recommend a 100% pure equity allocation to someone who has never experienced a market correction."
                    },
                    {
                        "lesson_id": "L11.02",
                        "title": "The Discipline of Rebalancing: Automated Buy-Low Sell-High",
                        "topic": "Restoring Equilibrium",
                        "format": "Mechanical Governor Animation + Case Study",
                        "duration": "14 mins",
                        "subtopics": [
                            "What is Portfolio Drift? An equity rally naturally turns a 60:40 portfolio into an exposed 75:25 portfolio",
                            "What is Rebalancing? Periodically trimming the outperforming asset and buying the lagging asset",
                            "The Psychological Genius: Rebalancing forces you to sell high and buy low without emotional forecasting",
                            "Annual Rebalancing vs. Threshold Rebalancing (e.g., when allocation drifts by >5% or >10%)",
                            "Tax and exit-load smart rebalancing: Using fresh SIP inflows or STP to rebalance without triggering redemptions"
                        ],
                        "know": "Rebalancing resets the portfolio back to its target risk level after market movements distort allocations.",
                        "understand": "Rebalancing feels emotionally counter-intuitive because it forces you to trim what just made the most money.",
                        "do": "Execute a rebalancing simulation on Turtlemint Pro moving profits from equity to debt after a 25% market rally.",
                        "say": "\"Rebalancing ped ki chhatayi jaisi hai—jo daali bohot lambi ho gayi use kaat kar jadon ko paani dena.\"",
                        "never_claim": "Never churn portfolios every month under the guise of rebalancing; once a year is optimal."
                    }
                ]
            }
        ]
    }
]
