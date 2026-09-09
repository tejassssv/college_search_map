import folium
from folium import Marker, plugins

map=folium.Map(location =[20.5937,78.9629],zoom_start=4.6) 
# 1. Your original data
colleges_data = [
    {
        "n": "NLSIU Bengaluru", "lt": 12.9592, "ln": 77.5113,
        "category": "Government", "location": {"city": "Bengaluru", "state": "Karnataka"},
        "weather": "Moderate, pleasant year-round.", "general_description": "India's undisputed #1 law school; premier corporate law placements.",
        "exam_required": "CLAT", "cutoff": "Rank 1 - 100", "average_package": "₹16.0 LPA"
    },
    {
        "n": "NALSAR Hyderabad", "lt": 17.5925, "ln": 78.5583,
        "category": "Government", "location": {"city": "Hyderabad", "state": "Telangana"},
        "weather": "Semi-arid, hot summers.", "general_description": "Known for outstanding liberal academic culture and moot court dominance.",
        "exam_required": "CLAT", "cutoff": "Rank < 200", "average_package": "₹15.5 LPA"
    },
    {
        "n": "NLU Delhi", "lt": 28.5996, "ln": 77.0270,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons (hot summers, cold winters).", "general_description": "Premier independent law university; Supreme Court proximity advantage.",
        "exam_required": "AILET", "cutoff": "Rank < 80", "average_package": "₹18.0 LPA"
    },
    {
        "n": "WBNUJS Kolkata", "lt": 22.5697, "ln": 88.4037,
        "category": "Government", "location": {"city": "Kolkata", "state": "West Bengal"},
        "weather": "Tropical wet and dry.", "general_description": "Top-tier corporate and international arbitration placement track record.",
        "exam_required": "CLAT", "cutoff": "Rank < 300", "average_package": "₹15.0 LPA"
    },
    {
        "n": "JGLS Sonipat", "lt": 28.9863, "ln": 77.0658,
        "category": "Private", "location": {"city": "Sonipat", "state": "Haryana"},
        "weather": "Semi-arid, extreme seasons.", "general_description": "Global faculty, world-class infrastructure, high international ties.",
        "exam_required": "LSAT-India", "cutoff": "80+ Percentile", "average_package": "₹11.5 LPA"
    },
    {
        "n": "NLU Jodhpur", "lt": 26.2415, "ln": 73.0337,
        "category": "Government", "location": {"city": "Jodhpur", "state": "Rajasthan"},
        "weather": "Hot desert climate.", "general_description": "Renowned for Corporate & IP law specializations.",
        "exam_required": "CLAT", "cutoff": "Rank < 400", "average_package": "₹14.5 LPA"
    },
    {
        "n": "GNLU Gandhinagar", "lt": 23.1895, "ln": 72.6358,
        "category": "Government", "location": {"city": "Gandhinagar", "state": "Gujarat"},
        "weather": "Hot semi-arid.", "general_description": "Vast campus with specialized research centers and maritime law focus.",
        "exam_required": "CLAT", "cutoff": "Rank < 500", "average_package": "₹14.0 LPA"
    },
    {
        "n": "Symbiosis Law School (SLS)", "lt": 18.5517, "ln": 73.9142,
        "category": "Private", "location": {"city": "Pune", "state": "Maharashtra"},
        "weather": "Pleasant tropical.", "general_description": "Top private law school in Western India with strong alumni base.",
        "exam_required": "SLAT", "cutoff": "Score 45+/60", "average_package": "₹11.0 LPA"
    },
    {
        "n": "Faculty of Law, DU", "lt": 28.6908, "ln": 77.2138,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Produced numerous Chief Justices of India and union ministers.",
        "exam_required": "CUET-PG", "cutoff": "Top 1%", "average_package": "₹10.0 LPA"
    },
    {
        "n": "NLIU Bhopal", "lt": 23.1610, "ln": 77.4014,
        "category": "Government", "location": {"city": "Bhopal", "state": "Madhya Pradesh"},
        "weather": "Humid subtropical.", "general_description": "Strong cyber law and judicial services track record.",
        "exam_required": "CLAT", "cutoff": "Rank < 600", "average_package": "₹13.0 LPA"
    },
    {
        "n": "MNLU Mumbai", "lt": 19.1232, "ln": 72.9090,
        "category": "Government", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical humid.", "general_description": "Rapid growth due to direct access to Mumbai's top law firms.",
        "exam_required": "CLAT", "cutoff": "Rank < 650", "average_package": "₹12.5 LPA"
    },
    {
        "n": "RMLNLU Lucknow", "lt": 26.7865, "ln": 80.9168,
        "category": "Government", "location": {"city": "Lucknow", "state": "Uttar Pradesh"},
        "weather": "Humid subtropical.", "general_description": "Known for constitutional law research and state judicial entries.",
        "exam_required": "CLAT", "cutoff": "Rank < 800", "average_package": "₹10.5 LPA"
    },
    {
        "n": "RGNUL Patiala", "lt": 30.3541, "ln": 76.3633,
        "category": "Government", "location": {"city": "Patiala", "state": "Punjab"},
        "weather": "Subtropical.", "general_description": "Sprawling infrastructure and expanding corporate placements.",
        "exam_required": "CLAT", "cutoff": "Rank < 1100", "average_package": "₹10.0 LPA"
    },
    {
        "n": "NUALS Kochi", "lt": 10.0487, "ln": 76.3533,
        "category": "Government", "location": {"city": "Kochi", "state": "Kerala"},
        "weather": "Tropical monsoon.", "general_description": "Strong maritime and environmental law research.",
        "exam_required": "CLAT", "cutoff": "Rank < 1300", "average_package": "₹9.5 LPA"
    },
    {
        "n": "NLUO Cuttack", "lt": 20.4883, "ln": 85.8770,
        "category": "Government", "location": {"city": "Cuttack", "state": "Odisha"},
        "weather": "Hot and humid.", "general_description": "Recognized for strong mooting achievements and legal aid clinics.",
        "exam_required": "CLAT", "cutoff": "Rank < 1200", "average_package": "₹11.0 LPA"
    },
    {
        "n": "NUSRL Ranchi", "lt": 23.3700, "ln": 85.3300,
        "category": "Government", "location": {"city": "Ranchi", "state": "Jharkhand"},
        "weather": "Pleasant subtropical.", "general_description": "Focus on mining, tribal, and constitutional jurisprudence.",
        "exam_required": "CLAT", "cutoff": "Rank < 1600", "average_package": "₹9.0 LPA"
    },
    {
        "n": "ILS Law College", "lt": 18.5165, "ln": 73.8300,
        "category": "Government", "location": {"city": "Pune", "state": "Maharashtra"},
        "weather": "Pleasant tropical.", "general_description": "Historic institution founded in 1924 with massive litigation alumni.",
        "exam_required": "MH CET Law", "cutoff": "99+ Percentile", "average_package": "₹8.5 LPA"
    },
    {
        "n": "GLC Mumbai", "lt": 18.9322, "ln": 72.8288,
        "category": "Government", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical humid.", "general_description": "Asia's oldest law school; exceptional Bombay High Court internship access.",
        "exam_required": "MH CET Law", "cutoff": "99.5+ Percentile", "average_package": "₹9.0 LPA"
    },
    {
        "n": "CNLU Patna", "lt": 25.5941, "ln": 85.1376,
        "category": "Government", "location": {"city": "Patna", "state": "Bihar"},
        "weather": "Humid subtropical.", "general_description": "Renowned for judicial services preparation and public law.",
        "exam_required": "CLAT", "cutoff": "Rank < 1500", "average_package": "₹8.5 LPA"
    },
    {
        "n": "DSNLU Visakhapatnam", "lt": 17.7291, "ln": 83.3087,
        "category": "Government", "location": {"city": "Visakhapatnam", "state": "Andhra Pradesh"},
        "weather": "Tropical coastal.", "general_description": "Growing corporate placement network across southern metro hubs.",
        "exam_required": "CLAT", "cutoff": "Rank < 1700", "average_package": "₹8.0 LPA"
    },
    {
        "n": "TNNLU Tiruchirappalli", "lt": 10.8225, "ln": 78.6946,
        "category": "Government", "location": {"city": "Tiruchirappalli", "state": "Tamil Nadu"},
        "weather": "Hot and dry.", "general_description": "Modern campus with extensive legal research infrastructure.",
        "exam_required": "CLAT", "cutoff": "Rank < 1900", "average_package": "₹8.0 LPA"
    },
    {
        "n": "AMU Faculty of Law", "lt": 27.9135, "ln": 78.0782,
        "category": "Government", "location": {"city": "Aligarh", "state": "Uttar Pradesh"},
        "weather": "Humid subtropical.", "general_description": "Historic legal center with affordable fees and strong litigation roots.",
        "exam_required": "AMU Law Entrance", "cutoff": "Top 1%", "average_package": "₹7.5 LPA"
    },
    {
        "n": "BHU Faculty of Law", "lt": 25.2677, "ln": 82.9913,
        "category": "Government", "location": {"city": "Varanasi", "state": "Uttar Pradesh"},
        "weather": "Subtropical.", "general_description": "Traditional powerhouse for civil and administrative law studies.",
        "exam_required": "CUET", "cutoff": "Top 2%", "average_package": "₹8.0 LPA"
    },
    {
        "n": "Jamia Millia Islamia Faculty of Law", "lt": 28.5616, "ln": 77.2802,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Consistently ranked among the top 10 legal faculties in India.",
        "exam_required": "JMI Law Entrance", "cutoff": "Top 1%", "average_package": "₹8.5 LPA"
    },
    {
        "n": "School of Law, Christ University", "lt": 12.9345, "ln": 77.6066,
        "category": "Private", "location": {"city": "Bengaluru", "state": "Karnataka"},
        "weather": "Pleasant.", "general_description": "Strong corporate legal cell and modern clinical training.",
        "exam_required": "CUET (Christ)", "cutoff": "High Merit", "average_package": "₹7.5 LPA"
    },
    {
        "n": "AIIMS New Delhi", "lt": 28.5672, "ln": 77.2100,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "India's premier apex medical institute and research hub.",
        "exam_required": "NEET-UG", "cutoff": "Rank 1 - 55", "average_package": "₹18.0 LPA"
    },
    {
        "n": "CMC Vellore", "lt": 12.9249, "ln": 79.1352,
        "category": "Private", "location": {"city": "Vellore", "state": "Tamil Nadu"},
        "weather": "Hot and dry.", "general_description": "Globally renowned healthcare pioneer; zero-commercialization ethos.",
        "exam_required": "NEET-UG", "cutoff": "Top Merit / Internal", "average_package": "₹12.0 LPA"
    },
    {
        "n": "JIPMER Puducherry", "lt": 11.9547, "ln": 79.8093,
        "category": "Government", "location": {"city": "Puducherry", "state": "Puducherry"},
        "weather": "Tropical coastal.", "general_description": "Institute of National Importance with autonomous research standing.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 250", "average_package": "₹15.0 LPA"
    },
    {
        "n": "NIMHANS Bengaluru", "lt": 12.9392, "ln": 77.5959,
        "category": "Government", "location": {"city": "Bengaluru", "state": "Karnataka"},
        "weather": "Pleasant year-round.", "general_description": "India's apex center for mental health and neurosciences.",
        "exam_required": "INI-CET", "cutoff": "Top INI-CET Ranks", "average_package": "₹16.0 LPA"
    },
    {
        "n": "KGMU Lucknow", "lt": 26.8687, "ln": 80.9167,
        "category": "Government", "location": {"city": "Lucknow", "state": "Uttar Pradesh"},
        "weather": "Humid subtropical.", "general_description": "Massive patient inflow and historic clinical legacy (1905).",
        "exam_required": "NEET-UG", "cutoff": "Rank < 1500", "average_package": "₹14.0 LPA"
    },
    {
        "n": "AIIMS Bhubaneswar", "lt": 20.2312, "ln": 85.7725,
        "category": "Government", "location": {"city": "Bhubaneswar", "state": "Odisha"},
        "weather": "Tropical humid.", "general_description": "Top-ranked among second-generation AIIMS institutions.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 600", "average_package": "₹15.0 LPA"
    },
    {
        "n": "AIIMS Jodhpur", "lt": 26.2415, "ln": 73.0112,
        "category": "Government", "location": {"city": "Jodhpur", "state": "Rajasthan"},
        "weather": "Hot desert climate.", "general_description": "Exceptional surgical training facilities and USMLE track records.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 500", "average_package": "₹15.5 LPA"
    },
    {
        "n": "AIIMS Rishikesh", "lt": 30.0758, "ln": 78.2882,
        "category": "Government", "location": {"city": "Rishikesh", "state": "Uttarakhand"},
        "weather": "Subtropical foothills.", "general_description": "Premier healthcare delivery and trauma center in northern India.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 800", "average_package": "₹14.5 LPA"
    },
    {
        "n": "AIIMS Bhopal", "lt": 23.2057, "ln": 77.4604,
        "category": "Government", "location": {"city": "Bhopal", "state": "Madhya Pradesh"},
        "weather": "Subtropical.", "general_description": "Central India's leading medical institute and super-specialty hospital.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 600", "average_package": "₹14.8 LPA"
    },
    {
        "n": "AIIMS Raipur", "lt": 21.2587, "ln": 81.5792,
        "category": "Government", "location": {"city": "Raipur", "state": "Chhattisgarh"},
        "weather": "Tropical.", "general_description": "High clinical case variety and modern medical research labs.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 1100", "average_package": "₹14.0 LPA"
    },
    {
        "n": "AIIMS Patna", "lt": 25.5604, "ln": 85.0441,
        "category": "Government", "location": {"city": "Patna", "state": "Bihar"},
        "weather": "Humid subtropical.", "general_description": "Rapidly growing super-specialty center in eastern India.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 1400", "average_package": "₹14.0 LPA"
    },
    {
        "n": "PGIMER Chandigarh", "lt": 30.7645, "ln": 76.7766,
        "category": "Government", "location": {"city": "Chandigarh", "state": "Chandigarh"},
        "weather": "Subtropical.", "general_description": "Postgraduate medical Mecca, leading in clinical research and fellowships.",
        "exam_required": "INI-CET", "cutoff": "Top INI-CET Ranks", "average_package": "₹17.0 LPA"
    },
    {
        "n": "Madras Medical College (MMC)", "lt": 13.0827, "ln": 80.2707,
        "category": "Government", "location": {"city": "Chennai", "state": "Tamil Nadu"},
        "weather": "Tropical humid.", "general_description": "One of Asia's oldest medical schools (1835) attached to RGGGH.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 1000", "average_package": "₹13.0 LPA"
    },
    {
        "n": "Grant Medical College (GMC)", "lt": 18.9616, "ln": 72.8336,
        "category": "Government", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical humid.", "general_description": "Affiliated with JJ Hospital; legendary bedside clinical exposure.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 1500", "average_package": "₹13.5 LPA"
    },
    {
        "n": "Seth GS Medical College (KEM)", "lt": 19.0016, "ln": 72.8427,
        "category": "Government", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical humid.", "general_description": "Extremely high NEET-UG cutoffs; high patient exposure in Mumbai.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 1000", "average_package": "₹14.5 LPA"
    },
    {
        "n": "Maulana Azad Medical College (MAMC)", "lt": 28.6366, "ln": 77.2407,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Top non-AIIMS government college in India, attached to LNJP Hospital.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 100", "average_package": "₹16.0 LPA"
    },
    {
        "n": "VMMC & Safdarjung Hospital", "lt": 28.5695, "ln": 77.2066,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Premier hospital complex with high clinical volumes and internal PG quota.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 150", "average_package": "₹16.0 LPA"
    },
    {
        "n": "Lady Hardinge Medical College (LHMC)", "lt": 28.6335, "ln": 77.2144,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Historic all-women undergraduate medical college centrally located in Delhi.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 550 (Female)", "average_package": "₹15.0 LPA"
    },
    {
        "n": "UCMS Delhi", "lt": 28.6836, "ln": 77.3090,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Associated with GTB Hospital; excellent residency and PG selections.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 350", "average_package": "₹15.5 LPA"
    },
    {
        "n": "IMS-BHU", "lt": 25.2750, "ln": 82.9995,
        "category": "Government", "location": {"city": "Varanasi", "state": "Uttar Pradesh"},
        "weather": "Subtropical.", "general_description": "Top-tier central medical institute within the sprawling BHU campus.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 900", "average_package": "₹15.0 LPA"
    },
    {
        "n": "Kasturba Medical College (KMC)", "lt": 13.3525, "ln": 74.7928,
        "category": "Private", "location": {"city": "Manipal", "state": "Karnataka"},
        "weather": "Tropical coastal.", "general_description": "India's highest-ranked private medical college; premier global alumni network.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 45000", "average_package": "₹10.5 LPA"
    },
    {
        "n": "St. John's Medical College", "lt": 12.9343, "ln": 77.6190,
        "category": "Private", "location": {"city": "Bengaluru", "state": "Karnataka"},
        "weather": "Pleasant.", "general_description": "Highly disciplined academic environment with strong community healthcare focus.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 12000", "average_package": "₹11.0 LPA"
    },
    {
        "n": "AFMC Pune", "lt": 18.5018, "ln": 73.8967,
        "category": "Government", "location": {"city": "Pune", "state": "Maharashtra"},
        "weather": "Pleasant tropical.", "general_description": "Produces commissioned medical officers for the Indian Armed Forces.",
        "exam_required": "NEET-UG + Interview", "cutoff": "Rank < 1500", "average_package": "₹16.5 LPA"
    },
    {
        "n": "Medical College Kolkata", "lt": 22.5735, "ln": 88.3629,
        "category": "Government", "location": {"city": "Kolkata", "state": "West Bengal"},
        "weather": "Tropical humid.", "general_description": "Oldest medical college in Asia (1835) with deep clinical traditions.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 2500", "average_package": "₹12.0 LPA"
    },
    {
        "n": "BJ Government Medical College", "lt": 18.5283, "ln": 73.8742,
        "category": "Government", "location": {"city": "Pune", "state": "Maharashtra"},
        "weather": "Pleasant tropical.", "general_description": "Associated with Sassoon General Hospital; high clinical surgical exposure.",
        "exam_required": "NEET-UG", "cutoff": "Rank < 2200", "average_package": "₹12.5 LPA"
    },
    {
        "n": "IIM Ahmedabad", "lt": 23.0325, "ln": 72.5312,
        "category": "Government", "location": {"city": "Ahmedabad", "state": "Gujarat"},
        "weather": "Hot semi-arid.", "general_description": "India's apex management school, famous for the rigorous Harvard Case Study method.",
        "exam_required": "CAT", "cutoff": "99.5+ Percentile", "average_package": "₹34.5 LPA"
    },
    {
        "n": "IIM Bangalore", "lt": 12.8954, "ln": 77.6000,
        "category": "Government", "location": {"city": "Bengaluru", "state": "Karnataka"},
        "weather": "Pleasant year-round.", "general_description": "Silicon Valley of India advantage; unmatched in tech, product, and strategy roles.",
        "exam_required": "CAT", "cutoff": "99.3+ Percentile", "average_package": "₹35.3 LPA"
    },
    {
        "n": "IIM Calcutta", "lt": 22.4497, "ln": 88.3073,
        "category": "Government", "location": {"city": "Kolkata", "state": "West Bengal"},
        "weather": "Tropical wet and dry.", "general_description": "Asia's finest finance campus, dominating quantitative finance and investment banking.",
        "exam_required": "CAT", "cutoff": "99.4+ Percentile", "average_package": "₹35.1 LPA"
    },
    {
        "n": "IIM Lucknow", "lt": 26.9238, "ln": 80.9329,
        "category": "Government", "location": {"city": "Lucknow", "state": "Uttar Pradesh"},
        "weather": "Humid subtropical.", "general_description": "Known for high academic pressure, consulting, and market research dominance.",
        "exam_required": "CAT", "cutoff": "98.5+ Percentile", "average_package": "₹32.2 LPA"
    },
    {
        "n": "IIM Kozhikode", "lt": 11.2858, "ln": 75.8742,
        "category": "Government", "location": {"city": "Kozhikode", "state": "Kerala"},
        "weather": "Tropical monsoon.", "general_description": "Scenic hilltop campus; pioneer in gender diversity and digital governance.",
        "exam_required": "CAT", "cutoff": "98.0+ Percentile", "average_package": "₹31.0 LPA"
    },
    {
        "n": "IIM Indore", "lt": 22.6583, "ln": 75.7956,
        "category": "Government", "location": {"city": "Indore", "state": "Madhya Pradesh"},
        "weather": "Pleasant winters.", "general_description": "Triple-crown accredited campus (AACSB, AMBA, EQUIS) with strong GM roles.",
        "exam_required": "CAT", "cutoff": "97.5+ Percentile", "average_package": "₹30.2 LPA"
    },
    {
        "n": "XLRI Jamshedpur", "lt": 22.8024, "ln": 86.1954,
        "category": "Private", "location": {"city": "Jamshedpur", "state": "Jharkhand"},
        "weather": "Tropical.", "general_description": "India's oldest B-school (1949); undisputed #1 for Human Resource Management (HRM).",
        "exam_required": "XAT", "cutoff": "96.0+ Percentile", "average_package": "₹32.7 LPA"
    },
    {
        "n": "FMS Delhi", "lt": 28.6874, "ln": 77.2081,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Highest ROI B-school in the world (~₹2 Lakhs total fees for ₹34 LPA package).",
        "exam_required": "CAT", "cutoff": "99.0+ Percentile", "average_package": "₹34.1 LPA"
    },
    {
        "n": "SPJIMR Mumbai", "lt": 19.1232, "ln": 72.8361,
        "category": "Private", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical humid.", "general_description": "Renowned for Autumn Internships and value-based leadership programs.",
        "exam_required": "CAT / XAT", "cutoff": "85+ Percentile (Profile)", "average_package": "₹33.0 LPA"
    },
    {
        "n": "ISB Hyderabad", "lt": 17.4260, "ln": 78.3428,
        "category": "Private", "location": {"city": "Hyderabad", "state": "Telangana"},
        "weather": "Semi-arid.", "general_description": "Top 1-year Executive MBA in Asia; partnership with Wharton and Kellogg.",
        "exam_required": "GMAT / GRE", "cutoff": "710+ GMAT", "average_package": "₹34.2 LPA"
    },
    {
        "n": "JBIMS Mumbai", "lt": 18.9304, "ln": 72.8277,
        "category": "Government", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical humid.", "general_description": "The 'CEO Factory' of India with massive corporate CXO alumni in Mumbai.",
        "exam_required": "MAH-CET / CAT", "cutoff": "99.99 Percentile", "average_package": "₹28.0 LPA"
    },
    {
        "n": "MDI Gurgaon", "lt": 28.4732, "ln": 77.0504,
        "category": "Private", "location": {"city": "Gurugram", "state": "Haryana"},
        "weather": "Semi-arid, extreme seasons.", "general_description": "Located directly inside the NCR corporate hub; outstanding marketing roles.",
        "exam_required": "CAT", "cutoff": "95.0+ Percentile", "average_package": "₹27.6 LPA"
    },
    {
        "n": "IIFT Delhi", "lt": 28.5440, "ln": 77.1950,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Ministry of Commerce institute; market leader in International Business & Trade.",
        "exam_required": "CAT", "cutoff": "97.5+ Percentile", "average_package": "₹29.1 LPA"
    },
    {
        "n": "IIM Shillong", "lt": 25.5788, "ln": 91.8933,
        "category": "Government", "location": {"city": "Shillong", "state": "Meghalaya"},
        "weather": "Cool, pleasant.", "general_description": "Rapidly emerging 2nd generation IIM with high corporate placement growth.",
        "exam_required": "CAT", "cutoff": "93.0+ Percentile", "average_package": "₹26.1 LPA"
    },
    {
        "n": "SJMSoM, IIT Bombay", "lt": 19.1334, "ln": 72.9133,
        "category": "Government", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical humid.", "general_description": "Elite operations, supply chain, and IT consulting placement records.",
        "exam_required": "CAT", "cutoff": "98.5+ Percentile", "average_package": "₹28.8 LPA"
    },
    {
        "n": "DMS, IIT Delhi", "lt": 28.5440, "ln": 77.1906,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "High ROI management school focusing on tech management and analytics.",
        "exam_required": "CAT", "cutoff": "98.0+ Percentile", "average_package": "₹25.8 LPA"
    },
    {
        "n": "VGSoM, IIT Kharagpur", "lt": 22.3149, "ln": 87.3105,
        "category": "Government", "location": {"city": "Kharagpur", "state": "West Bengal"},
        "weather": "Tropical.", "general_description": "Oldest IIT management school; excellent operations and data analytics profiles.",
        "exam_required": "CAT", "cutoff": "95.0+ Percentile", "average_package": "₹22.1 LPA"
    },
    {
        "n": "IIM Mumbai (NITIE)", "lt": 19.1384, "ln": 72.9038,
        "category": "Government", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical humid.", "general_description": "Formerly NITIE; unmatched leader in supply chain and manufacturing operations.",
        "exam_required": "CAT", "cutoff": "97.0+ Percentile", "average_package": "₹31.0 LPA"
    },
    {
        "n": "IIM Ranchi", "lt": 23.3441, "ln": 85.3096,
        "category": "Government", "location": {"city": "Ranchi", "state": "Jharkhand"},
        "weather": "Pleasant subtropical.", "general_description": "Top-performing second-generation IIM with a strong dedicated HR program.",
        "exam_required": "CAT", "cutoff": "94.0+ Percentile", "average_package": "₹17.3 LPA"
    },
    {
        "n": "IIM Raipur", "lt": 21.1444, "ln": 81.7656,
        "category": "Government", "location": {"city": "Raipur", "state": "Chhattisgarh"},
        "weather": "Tropical.", "general_description": "Modern state-of-the-art campus in Naya Raipur with growing brand equity.",
        "exam_required": "CAT", "cutoff": "93.5+ Percentile", "average_package": "₹21.0 LPA"
    },
    {
        "n": "IIM Trichy", "lt": 10.7099, "ln": 78.7778,
        "category": "Government", "location": {"city": "Tiruchirappalli", "state": "Tamil Nadu"},
        "weather": "Hot and dry.", "general_description": "Known for academic depth in finance and strong corporate partnerships.",
        "exam_required": "CAT", "cutoff": "94.0+ Percentile", "average_package": "₹20.5 LPA"
    },
    {
        "n": "IIM Udaipur", "lt": 24.5362, "ln": 73.6934,
        "category": "Government", "location": {"city": "Udaipur", "state": "Rajasthan"},
        "weather": "Hot semi-arid.", "general_description": "Global research orientation with stellar supply chain management center.",
        "exam_required": "CAT", "cutoff": "93.0+ Percentile", "average_package": "₹20.3 LPA"
    },
    {
        "n": "NMIMS Mumbai (SBM)", "lt": 19.1030, "ln": 72.8368,
        "category": "Private", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical humid.", "general_description": "Prime Mumbai location with massive FMCG and banking batch recruitments.",
        "exam_required": "NMAT", "cutoff": "Score 235+", "average_package": "₹26.6 LPA"
    },
    {
        "n": "SIBM Pune", "lt": 18.5308, "ln": 73.7431,
        "category": "Private", "location": {"city": "Pune", "state": "Maharashtra"},
        "weather": "Pleasant tropical.", "general_description": "Flagship Symbiosis institute; dominant in sales, marketing, and HR.",
        "exam_required": "SNAP", "cutoff": "98.5+ Percentile", "average_package": "₹26.7 LPA"
    },
    {
        "n": "TISS Mumbai (HRM & LR)", "lt": 19.0443, "ln": 72.9149,
        "category": "Government", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical humid.", "general_description": "Equivalent to XLRI for HR; phenomenal ROI with industry-topping packages.",
        "exam_required": "CUET-PG", "cutoff": "Top 1%", "average_package": "₹27.2 LPA"
    },

    # ==================== 23 IITs ====================

    {
        "n": "IIT Madras", "lt": 12.9915, "ln": 80.2337,
        "category": "Government", "location": {"city": "Chennai", "state": "Tamil Nadu"},
        "weather": "Hot and humid tropical climate.", "general_description": "NIRF #1 engineering institute, excellent research park.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~150", "average_package": "₹21.5 LPA"
    },
    {
        "n": "IIT Delhi", "lt": 28.5440, "ln": 77.1906,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme summers and cold winters.", "general_description": "Top-tier startup culture and capital city advantage.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~100", "average_package": "₹25.8 LPA"
    },
    {
        "n": "IIT Bombay", "lt": 19.1334, "ln": 72.9133,
        "category": "Government", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical, heavy monsoons.", "general_description": "Most sought-after IIT for top JEE rankers.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR 1-68", "average_package": "₹21.8 LPA"
    },
    {
        "n": "IIT Kanpur", "lt": 26.5123, "ln": 80.2329,
        "category": "Government", "location": {"city": "Kanpur", "state": "Uttar Pradesh"},
        "weather": "Hot summers, chilly winters.", "general_description": "Legendary academic rigor and coding culture.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~250", "average_package": "₹22.0 LPA"
    },
    {
        "n": "IIT Kharagpur", "lt": 22.3149, "ln": 87.3105,
        "category": "Government", "location": {"city": "Kharagpur", "state": "West Bengal"},
        "weather": "Tropical wet and dry.", "general_description": "Oldest and largest IIT campus.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~400", "average_package": "₹19.5 LPA"
    },
    {
        "n": "IIT Roorkee", "lt": 29.8649, "ln": 77.8966,
        "category": "Government", "location": {"city": "Roorkee", "state": "Uttarakhand"},
        "weather": "Humid subtropical, pleasant winters.", "general_description": "Historic campus, excellent core branches.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~450", "average_package": "₹18.3 LPA"
    },
    {
        "n": "IIT Guwahati", "lt": 26.1878, "ln": 91.6916,
        "category": "Government", "location": {"city": "Guwahati", "state": "Assam"},
        "weather": "Subtropical with heavy rain.", "general_description": "Most scenic campus, strong design/tech programs.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~650", "average_package": "₹19.2 LPA"
    },
    {
        "n": "IIT Hyderabad", "lt": 17.5947, "ln": 78.1228,
        "category": "Government", "location": {"city": "Sangareddy", "state": "Telangana"},
        "weather": "Semi-arid, hot summers.", "general_description": "Fastest-growing new IIT with strong AI focus.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~600", "average_package": "₹20.0 LPA"
    },
    {
        "n": "IIT Indore", "lt": 22.5204, "ln": 75.9207,
        "category": "Government", "location": {"city": "Indore", "state": "Madhya Pradesh"},
        "weather": "Pleasant winters, hot summers.", "general_description": "Excellent research and undergraduate facilities.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~1100", "average_package": "₹19.4 LPA"
    },
    {
        "n": "IIT (BHU) Varanasi", "lt": 25.2677, "ln": 82.9913,
        "category": "Government", "location": {"city": "Varanasi", "state": "Uttar Pradesh"},
        "weather": "Subtropical, extreme seasons.", "general_description": "Century-old legacy integrated into an IIT.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~1000", "average_package": "₹20.0 LPA"
    },
    {
        "n": "IIT (ISM) Dhanbad", "lt": 23.8143, "ln": 86.4412,
        "category": "Government", "location": {"city": "Dhanbad", "state": "Jharkhand"},
        "weather": "Warm and temperate.", "general_description": "Historic mining school now a premier IIT.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~2800", "average_package": "₹17.0 LPA"
    },
    {
        "n": "IIT Bhubaneswar", "lt": 20.1483, "ln": 85.6712,
        "category": "Government", "location": {"city": "Bhubaneswar", "state": "Odisha"},
        "weather": "Hot and humid.", "general_description": "Strong infrastructure and growing placement records.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~2700", "average_package": "₹16.1 LPA"
    },
    {
        "n": "IIT Gandhinagar", "lt": 23.2114, "ln": 72.6842,
        "category": "Government", "location": {"city": "Gandhinagar", "state": "Gujarat"},
        "weather": "Hot semi-arid.", "general_description": "Known for liberal arts integration and modern campus.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~1500", "average_package": "₹15.3 LPA"
    },
    {
        "n": "IIT Ropar", "lt": 30.9753, "ln": 76.5273,
        "category": "Government", "location": {"city": "Rupnagar", "state": "Punjab"},
        "weather": "Hot summers, cold winters.", "general_description": "Top new-gen IIT for research citations.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~1800", "average_package": "₹18.0 LPA"
    },
    {
        "n": "IIT Patna", "lt": 25.5357, "ln": 84.8510,
        "category": "Government", "location": {"city": "Patna", "state": "Bihar"},
        "weather": "Humid subtropical.", "general_description": "Exceptional coding culture among newer IITs.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~2600", "average_package": "₹28.5 LPA"
    },
    {
        "n": "IIT Mandi", "lt": 31.7754, "ln": 76.9861,
        "category": "Government", "location": {"city": "Mandi", "state": "Himachal Pradesh"},
        "weather": "Pleasant, cold winters.", "general_description": "Himalayan campus with interdisciplinary focus.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~3000", "average_package": "₹22.0 LPA"
    },
    {
        "n": "IIT Jodhpur", "lt": 26.4710, "ln": 73.1134,
        "category": "Government", "location": {"city": "Jodhpur", "state": "Rajasthan"},
        "weather": "Hot desert climate.", "general_description": "Strong focus on AI and data science.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~2400", "average_package": "₹17.0 LPA"
    },
    {
        "n": "IIT Tirupati", "lt": 13.6288, "ln": 79.4192,
        "category": "Government", "location": {"city": "Tirupati", "state": "Andhra Pradesh"},
        "weather": "Tropical.", "general_description": "Fastest developing 3rd gen IIT.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~3700", "average_package": "₹15.5 LPA"
    },
    {
        "n": "IIT Bhilai", "lt": 21.1610, "ln": 81.3323,
        "category": "Government", "location": {"city": "Bhilai", "state": "Chhattisgarh"},
        "weather": "Tropical wet and dry.", "general_description": "Growing core and IT sector placements.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~5100", "average_package": "₹14.0 LPA"
    },
    {
        "n": "IIT Goa", "lt": 15.3927, "ln": 73.9875,
        "category": "Government", "location": {"city": "Ponda", "state": "Goa"},
        "weather": "Tropical monsoon.", "general_description": "Temporary campus but strong IIT Bombay mentorship.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~4100", "average_package": "₹16.3 LPA"
    },
    {
        "n": "IIT Jammu", "lt": 32.8407, "ln": 74.8727,
        "category": "Government", "location": {"city": "Jammu", "state": "Jammu & Kashmir"},
        "weather": "Subtropical.", "general_description": "Scenic campus with rapidly improving stats.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~4600", "average_package": "₹15.0 LPA"
    },
    {
        "n": "IIT Dharwad", "lt": 15.4859, "ln": 74.9338,
        "category": "Government", "location": {"city": "Dharwad", "state": "Karnataka"},
        "weather": "Tropical wet and dry.", "general_description": "Benefiting from proximity to Bangalore IT hub.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~4700", "average_package": "₹16.0 LPA"
    },
    {
        "n": "IIT Palakkad", "lt": 10.8280, "ln": 76.6575,
        "category": "Government", "location": {"city": "Palakkad", "state": "Kerala"},
        "weather": "Humid tropical.", "general_description": "Permanent campus functional with growing tech culture.",
        "exam_required": "JEE Advanced", "cutoff": "CSE AIR ~4800", "average_package": "₹13.9 LPA"
    },

    # ==================== NITs ====================

    {
        "n": "NIT Trichy", "lt": 10.7628, "ln": 78.8159,
        "category": "Government", "location": {"city": "Tiruchirappalli", "state": "Tamil Nadu"},
        "weather": "Hot and dry.", "general_description": "Top-ranked NIT, comparable to older IITs.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~1500", "average_package": "₹15.7 LPA"
    },
    {
        "n": "NIT Surathkal", "lt": 13.0108, "ln": 74.7943,
        "category": "Government", "location": {"city": "Mangaluru", "state": "Karnataka"},
        "weather": "Coastal, heavy rain.", "general_description": "Private beach, exceptional IT placements.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~2000", "average_package": "₹16.5 LPA"
    },
    {
        "n": "NIT Warangal", "lt": 17.9835, "ln": 79.5305,
        "category": "Government", "location": {"city": "Warangal", "state": "Telangana"},
        "weather": "Semi-arid, hot.", "general_description": "First NIT, legendary coding culture.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~2200", "average_package": "₹15.9 LPA"
    },
    {
        "n": "NIT Calicut", "lt": 11.3216, "ln": 75.9336,
        "category": "Government", "location": {"city": "Kozhikode", "state": "Kerala"},
        "weather": "Tropical monsoon.", "general_description": "Excellent architecture and software branches.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~4500", "average_package": "₹12.5 LPA"
    },
    {
        "n": "NIT Rourkela", "lt": 22.2533, "ln": 84.9009,
        "category": "Government", "location": {"city": "Rourkela", "state": "Odisha"},
        "weather": "Tropical.", "general_description": "Largest NIT campus, vast core branch options.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~3500", "average_package": "₹13.3 LPA"
    },
    {
        "n": "MNIT Jaipur", "lt": 26.8633, "ln": 75.8106,
        "category": "Government", "location": {"city": "Jaipur", "state": "Rajasthan"},
        "weather": "Semi-arid.", "general_description": "Prime location with strong northern industry ties.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~4500", "average_package": "₹10.0 LPA"
    },
    {
        "n": "VNIT Nagpur", "lt": 21.1233, "ln": 79.0515,
        "category": "Government", "location": {"city": "Nagpur", "state": "Maharashtra"},
        "weather": "Tropical wet and dry.", "general_description": "Central location, highly active student bodies.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~5500", "average_package": "₹10.5 LPA"
    },
    {
        "n": "NIT Kurukshetra", "lt": 29.9482, "ln": 76.8174,
        "category": "Government", "location": {"city": "Kurukshetra", "state": "Haryana"},
        "weather": "Extreme summers and winters.", "general_description": "Strong placements in Delhi-NCR tech hub.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~6500", "average_package": "₹11.0 LPA"
    },
    {
        "n": "MNNIT Allahabad", "lt": 25.4930, "ln": 81.8624,
        "category": "Government", "location": {"city": "Prayagraj", "state": "Uttar Pradesh"},
        "weather": "Humid subtropical.", "general_description": "Highest coding averages among NITs.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~4000", "average_package": "₹16.0 LPA"
    },
    {
        "n": "NIT Durgapur", "lt": 23.5477, "ln": 87.2931,
        "category": "Government", "location": {"city": "Durgapur", "state": "West Bengal"},
        "weather": "Tropical.", "general_description": "Strong alumni base in eastern India.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~8500", "average_package": "₹11.5 LPA"
    },
    {
        "n": "NIT Silchar", "lt": 24.7577, "ln": 92.7923,
        "category": "Government", "location": {"city": "Silchar", "state": "Assam"},
        "weather": "Humid, rainy.", "general_description": "Beautiful campus with rapidly rising placements.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~10000", "average_package": "₹13.5 LPA"
    },
    {
        "n": "MANIT Bhopal", "lt": 23.2144, "ln": 77.4042,
        "category": "Government", "location": {"city": "Bhopal", "state": "Madhya Pradesh"},
        "weather": "Subtropical.", "general_description": "Centrally located, vast campus.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~7500", "average_package": "₹11.5 LPA"
    },
    {
        "n": "NIT Jalandhar", "lt": 31.3958, "ln": 75.5345,
        "category": "Government", "location": {"city": "Jalandhar", "state": "Punjab"},
        "weather": "Hot summers, cold winters.", "general_description": "Known for textile and core engineering.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~9500", "average_package": "₹11.6 LPA"
    },
    {
        "n": "NIT Jamshedpur", "lt": 22.7756, "ln": 86.1451,
        "category": "Government", "location": {"city": "Jamshedpur", "state": "Jharkhand"},
        "weather": "Tropical.", "general_description": "Incredible core placements due to Tata Steel proximity.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~8000", "average_package": "₹14.7 LPA"
    },
    {
        "n": "NIT Delhi", "lt": 28.8431, "ln": 77.1049,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Permanent campus active, huge location advantage.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~7000", "average_package": "₹15.9 LPA"
    },
    {
        "n": "NIT Hamirpur", "lt": 31.7084, "ln": 76.5274,
        "category": "Government", "location": {"city": "Hamirpur", "state": "Himachal Pradesh"},
        "weather": "Cool, pleasant.", "general_description": "Stunning hill-station campus.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~10500", "average_package": "₹10.5 LPA"
    },{
        "n": "NIT Raipur", "lt": 21.2497, "ln": 81.6050,
        "category": "Government", "location": {"city": "Raipur", "state": "Chhattisgarh"},
        "weather": "Tropical.", "general_description": "Urban campus, strong local mining/metallurgy ties.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~11500", "average_package": "₹10.1 LPA"
    },
    {
        "n": "NIT Agartala", "lt": 23.8406, "ln": 91.4215,
        "category": "Government", "location": {"city": "Agartala", "state": "Tripura"},
        "weather": "Humid subtropical.", "general_description": "Massive infrastructure development in Northeast.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~18000", "average_package": "₹8.5 LPA"
    },
    {
        "n": "NIT Goa", "lt": 15.3932, "ln": 73.9870,
        "category": "Government", "location": {"city": "Ponda", "state": "Goa"},
        "weather": "Tropical.", "general_description": "Smaller intake, high quality IT placements.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~12000", "average_package": "₹11.0 LPA"
    },
    {
        "n": "NIT Meghalaya", "lt": 25.5740, "ln": 91.8974,
        "category": "Government", "location": {"city": "Shillong", "state": "Meghalaya"},
        "weather": "Cool, heavy rain.", "general_description": "Best performing among newer Northeast NITs.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~16000", "average_package": "₹8.0 LPA"
    },
    {
        "n": "NIT Patna", "lt": 25.6208, "ln": 85.1720,
        "category": "Government", "location": {"city": "Patna", "state": "Bihar"},
        "weather": "Humid subtropical.", "general_description": "6th oldest engineering college in India.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~13500", "average_package": "₹9.5 LPA"
    },
    {
        "n": "NIT Srinagar", "lt": 34.1207, "ln": 74.8378,
        "category": "Government", "location": {"city": "Srinagar", "state": "Jammu & Kashmir"},
        "weather": "Cold, snowy winters.", "general_description": "Scenic campus by Dal Lake.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~22000", "average_package": "₹8.5 LPA"
    },
    {
        "n": "NIT Puducherry", "lt": 10.9631, "ln": 79.8451,
        "category": "Government", "location": {"city": "Karaikal", "state": "Puducherry"},
        "weather": "Tropical coastal.", "general_description": "Growing south Indian NIT.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~15000", "average_package": "₹8.4 LPA"
    },
    {
        "n": "NIT Manipur", "lt": 24.8193, "ln": 93.9372,
        "category": "Government", "location": {"city": "Imphal", "state": "Manipur"},
        "weather": "Subtropical.", "general_description": "Developing infrastructure in scenic Northeast.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~25000", "average_package": "₹7.5 LPA"
    },
    {
        "n": "NIT Arunachal Pradesh", "lt": 27.1350, "ln": 93.7314,
        "category": "Government", "location": {"city": "Yupia", "state": "Arunachal Pradesh"},
        "weather": "Cool and rainy.", "general_description": "Focus on core academics and hill development.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~28000", "average_package": "₹6.8 LPA"
    },
    {
        "n": "NIT Mizoram", "lt": 23.7299, "ln": 92.7231,
        "category": "Government", "location": {"city": "Aizawl", "state": "Mizoram"},
        "weather": "Mild, pleasant.", "general_description": "Temporary campus, strong focus on CS.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~29000", "average_package": "₹6.5 LPA"
    },
    {
        "n": "NIT Sikkim", "lt": 27.3117, "ln": 88.3615,
        "category": "Government", "location": {"city": "Ravangla", "state": "Sikkim"},
        "weather": "Cold, alpine.", "general_description": "High altitude campus.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~27000", "average_package": "₹7.0 LPA"
    },
    {
        "n": "NIT Uttarakhand", "lt": 30.2198, "ln": 78.7844,
        "category": "Government", "location": {"city": "Srinagar", "state": "Uttarakhand"},
        "weather": "Mountainous, cold.", "general_description": "Hill state NIT with growing intake.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~17000", "average_package": "₹8.5 LPA"
    },
    {
        "n": "NIT Nagaland", "lt": 25.7766, "ln": 93.7663,
        "category": "Government", "location": {"city": "Dimapur", "state": "Nagaland"},
        "weather": "Tropical.", "general_description": "Emerging NIT in the Northeast.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~31000", "average_package": "₹6.2 LPA"
    },
    {
        "n": "NIT Andhra Pradesh", "lt": 16.8118, "ln": 81.5283,
        "category": "Government", "location": {"city": "Tadepalligudem", "state": "Andhra Pradesh"},
        "weather": "Hot and humid.", "general_description": "Newest NIT, rapidly building permanent campus.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~18000", "average_package": "₹7.5 LPA"
    },
    {
        "n": "SVNIT Surat", "lt": 21.1633, "ln": 72.7842,
        "category": "Government", "location": {"city": "Surat", "state": "Gujarat"},
        "weather": "Tropical, humid.", "general_description": "High placements due to Gujarat industrial belt.",
        "exam_required": "JEE Main", "cutoff": "CSE AIR ~6000", "average_package": "₹12.0 LPA"
    },

    # ==================== BITS & VITs ====================

    {
        "n": "BITS Pilani", "lt": 28.3639, "ln": 75.5870,
        "category": "Private", "location": {"city": "Pilani", "state": "Rajasthan"},
        "weather": "Desert climate.", "general_description": "India's #1 private college, zero attendance policy.",
        "exam_required": "BITSAT", "cutoff": "Score ~330/390 (CSE)", "average_package": "₹20.5 LPA"
    },
    {
        "n": "BITS Goa", "lt": 15.3911, "ln": 73.8782,
        "category": "Private", "location": {"city": "Zuarinagar", "state": "Goa"},
        "weather": "Tropical coastal.", "general_description": "Excellent coding culture and GSoC selections.",
        "exam_required": "BITSAT", "cutoff": "Score ~300/390 (CSE)", "average_package": "₹18.5 LPA"
    },
    {
        "n": "BITS Hyderabad", "lt": 17.5449, "ln": 78.5718,
        "category": "Private", "location": {"city": "Hyderabad", "state": "Telangana"},
        "weather": "Semi-arid.", "general_description": "Modern campus with brilliant tech labs.",
        "exam_required": "BITSAT", "cutoff": "Score ~295/390 (CSE)", "average_package": "₹18.0 LPA"
    },
    {
        "n": "VIT Vellore", "lt": 12.9692, "ln": 79.1559,
        "category": "Private", "location": {"city": "Vellore", "state": "Tamil Nadu"},
        "weather": "Hot and dry.", "general_description": "Massive student body, FFCS credit system.",
        "exam_required": "VITEEE", "cutoff": "Rank <2000 (CSE Cat 1)", "average_package": "₹9.2 LPA"
    },
    {
        "n": "VIT Chennai", "lt": 12.8406, "ln": 80.1534,
        "category": "Private", "location": {"city": "Chennai", "state": "Tamil Nadu"},
        "weather": "Hot and humid.", "general_description": "Shares placement cell with Vellore.",
        "exam_required": "VITEEE", "cutoff": "Rank <8000 (CSE Cat 1)", "average_package": "₹8.8 LPA"
    },
    {
        "n": "VIT-AP", "lt": 16.4950, "ln": 80.5000,
        "category": "Private", "location": {"city": "Amaravati", "state": "Andhra Pradesh"},
        "weather": "Tropical.", "general_description": "Fast-growing new campus.",
        "exam_required": "VITEEE", "cutoff": "Rank <35000", "average_package": "₹7.5 LPA"
    },
    {
        "n": "VIT Bhopal", "lt": 23.0772, "ln": 76.8513,
        "category": "Private", "location": {"city": "Bhopal", "state": "Madhya Pradesh"},
        "weather": "Subtropical.", "general_description": "100% doctoral faculty.",
        "exam_required": "VITEEE", "cutoff": "Rank <45000", "average_package": "₹7.2 LPA"
    },

    # ==================== Other Premier Colleges ====================

    {
        "n": "IIIT Hyderabad", "lt": 17.4455, "ln": 78.3483,
        "category": "Government", "location": {"city": "Hyderabad", "state": "Telangana"},
        "weather": "Semi-arid.", "general_description": "Top coding institute in India, rivals IIT Bombay CSE.",
        "exam_required": "JEE Main / UGEE", "cutoff": "AIR <1000", "average_package": "₹32.0 LPA"
    },
    {
        "n": "IIIT Bangalore", "lt": 12.8447, "ln": 77.6633,
        "category": "Government", "location": {"city": "Bengaluru", "state": "Karnataka"},
        "weather": "Pleasant year-round.", "general_description": "Offers integrated MTech with elite IT placements.",
        "exam_required": "JEE Main", "cutoff": "AIR <7500", "average_package": "₹30.7 LPA"
    },
    {
        "n": "IIIT Delhi", "lt": 28.5459, "ln": 77.2732,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Top-tier AI and CS research state university.",
        "exam_required": "JEE Main (JAC)", "cutoff": "AIR <12000", "average_package": "₹23.7 LPA"
    },
    {
        "n": "IIIT Allahabad", "lt": 25.4300, "ln": 81.7715,
        "category": "Government", "location": {"city": "Prayagraj", "state": "Uttar Pradesh"},
        "weather": "Humid subtropical.", "general_description": "Dominates competitive programming circuits.",
        "exam_required": "JEE Main", "cutoff": "AIR <5000", "average_package": "₹18.5 LPA"
    },
    {
        "n": "ABV-IIITM Gwalior", "lt": 26.2495, "ln": 78.1738,
        "category": "Government", "location": {"city": "Gwalior", "state": "Madhya Pradesh"},
        "weather": "Subtropical.", "general_description": "First IIIT, offers IT + MBA integrated courses.",
        "exam_required": "JEE Main", "cutoff": "AIR <7000", "average_package": "₹24.3 LPA"
    },
    {
        "n": "IIITDM Jabalpur", "lt": 23.1764, "ln": 80.0205,
        "category": "Government", "location": {"city": "Jabalpur", "state": "Madhya Pradesh"},
        "weather": "Humid subtropical.", "general_description": "Focuses on design and manufacturing.",
        "exam_required": "JEE Main", "cutoff": "AIR <14000", "average_package": "₹14.0 LPA"
    },
    {
        "n": "IIITDM Kancheepuram", "lt": 12.8379, "ln": 80.1378,
        "category": "Government", "location": {"city": "Chennai", "state": "Tamil Nadu"},
        "weather": "Tropical.", "general_description": "Strong core and design integration.",
        "exam_required": "JEE Main", "cutoff": "AIR <16000", "average_package": "₹11.0 LPA"
    },
    {
        "n": "IIIT Pune", "lt": 18.5204, "ln": 73.8567,
        "category": "Government", "location": {"city": "Pune", "state": "Maharashtra"},
        "weather": "Tropical wet and dry.", "general_description": "Rapidly growing IT stats due to Pune hub.",
        "exam_required": "JEE Main", "cutoff": "AIR <15000", "average_package": "₹16.8 LPA"
    },
    {
        "n": "IIIT Lucknow", "lt": 26.8043, "ln": 81.0215,
        "category": "Government", "location": {"city": "Lucknow", "state": "Uttar Pradesh"},
        "weather": "Humid subtropical.", "general_description": "Incredible placement growth in recent years.",
        "exam_required": "JEE Main", "cutoff": "AIR <10000", "average_package": "₹30.5 LPA"
    },
    {
        "n": "Jadavpur University", "lt": 22.4989, "ln": 88.3714,
        "category": "Government", "location": {"city": "Kolkata", "state": "West Bengal"},
        "weather": "Tropical wet and dry.", "general_description": "Best ROI in India (₹10K total fees).",
        "exam_required": "WBJEE", "cutoff": "Rank 1-100 (CSE)", "average_package": "₹10.5 LPA"
    },
    {
        "n": "DTU", "lt": 28.7499, "ln": 77.1180,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Massive tech alumni network.",
        "exam_required": "JEE Main (JAC)", "cutoff": "AIR <10000 (Delhi)", "average_package": "₹15.0 LPA"
    },
    {
        "n": "NSUT", "lt": 28.6095, "ln": 77.0353,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Shares elite status with DTU in capital.",
        "exam_required": "JEE Main (JAC)", "cutoff": "AIR <12000 (Delhi)", "average_package": "₹14.0 LPA"
    },
    {
        "n": "IIEST Shibpur", "lt": 22.5562, "ln": 88.3073,
        "category": "Government", "location": {"city": "Howrah", "state": "West Bengal"},
        "weather": "Tropical.", "general_description": "One of India's oldest institutes (1856).",
        "exam_required": "JEE Main", "cutoff": "AIR <20000", "average_package": "₹11.0 LPA"
    },
    {
        "n": "COEP Pune", "lt": 18.5293, "ln": 73.8565,
        "category": "Government", "location": {"city": "Pune", "state": "Maharashtra"},
        "weather": "Pleasant.", "general_description": "Historic Maharashtra engineering college.",
        "exam_required": "MHT-CET / JEE Main", "cutoff": "99.8+ Percentile", "average_package": "₹11.0 LPA"
    },
    {
        "n": "VJTI Mumbai", "lt": 19.0222, "ln": 72.8561,
        "category": "Government", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical.", "general_description": "Mumbai's premier state college.",
        "exam_required": "MHT-CET", "cutoff": "99.9+ Percentile", "average_package": "₹14.0 LPA"
    },
    {
        "n": "ICT Mumbai", "lt": 19.0232, "ln": 72.8580,
        "category": "Government", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical.", "general_description": "Asia's best chemical engineering institute.",
        "exam_required": "MHT-CET", "cutoff": "99.5+ Percentile", "average_package": "₹9.0 LPA"
    },
    {
        "n": "CEG Anna Univ", "lt": 13.0102, "ln": 80.2354,
        "category": "Government", "location": {"city": "Chennai", "state": "Tamil Nadu"},
        "weather": "Tropical.", "general_description": "Top state college in Tamil Nadu.",
        "exam_required": "TNEA (12th Marks)", "cutoff": "199.5+/200", "average_package": "₹8.5 LPA"
    },
    {
        "n": "MIT Chennai", "lt": 12.9490, "ln": 80.1385,
        "category": "Government", "location": {"city": "Chennai", "state": "Tamil Nadu"},
        "weather": "Tropical.", "general_description": "APJ Abdul Kalam's alma mater.",
        "exam_required": "TNEA", "cutoff": "199+/200", "average_package": "₹8.0 LPA"
    },
    {
        "n": "PEC Chandigarh", "lt": 30.7673, "ln": 76.7865,
        "category": "Government", "location": {"city": "Chandigarh", "state": "Chandigarh"},
        "weather": "Subtropical.", "general_description": "Kalpana Chawla's alma mater.",
        "exam_required": "JEE Main", "cutoff": "AIR <15000", "average_package": "₹13.5 LPA"
    },
    {
        "n": "Thapar Institute", "lt": 30.3541, "ln": 76.3633,
        "category": "Private", "location": {"city": "Patiala", "state": "Punjab"},
        "weather": "Subtropical.", "general_description": "High tier private university with strong alumni.",
        "exam_required": "JEE Main / 12th Marks", "cutoff": "AIR <40000", "average_package": "₹11.9 LPA"
    },
    {
        "n": "Manipal (MIT)", "lt": 13.3525, "ln": 74.7928,
        "category": "Private", "location": {"city": "Manipal", "state": "Karnataka"},
        "weather": "Tropical coastal.", "general_description": "Satya Nadella's alma mater, great campus life.",
        "exam_required": "MET", "cutoff": "Rank <1000 (CSE)", "average_package": "₹12.5 LPA"
    },
    {
        "n": "DA-IICT", "lt": 23.1885, "ln": 72.6283,
        "category": "Private", "location": {"city": "Gandhinagar", "state": "Gujarat"},
        "weather": "Semi-arid.", "general_description": "Gujarat's top IT and communication college.",
        "exam_required": "JEE Main", "cutoff": "AIR <15000", "average_package": "₹17.0 LPA"
    },
    {
        "n": "RVCE", "lt": 12.9237, "ln": 77.4987,
        "category": "Private", "location": {"city": "Bengaluru", "state": "Karnataka"},
        "weather": "Pleasant.", "general_description": "Top COMEDK college in Bangalore.",
        "exam_required": "KCET / COMEDK", "cutoff": "Rank <300 (COMEDK)", "average_package": "₹13.0 LPA"
    },
    {
        "n": "BMSCE", "lt": 12.9410, "ln": 77.5655,
        "category": "Private", "location": {"city": "Bengaluru", "state": "Karnataka"},
        "weather": "Pleasant.", "general_description": "Highly reputed private Bangalore college.",
        "exam_required": "KCET / COMEDK", "cutoff": "Rank <1000 (COMEDK)", "average_package": "₹9.5 LPA"
    },
    {
        "n": "MSRIT", "lt": 13.0285, "ln": 77.5698,
        "category": "Private", "location": {"city": "Bengaluru", "state": "Karnataka"},
        "weather": "Pleasant.", "general_description": "Excellent industry ties in IT capital.",
        "exam_required": "KCET / COMEDK", "cutoff": "Rank <1500 (COMEDK)", "average_package": "₹9.0 LPA"
    },
    {
        "n": "PSG College", "lt": 11.0247, "ln": 77.0028,
        "category": "Private", "location": {"city": "Coimbatore", "state": "Tamil Nadu"},
        "weather": "Tropical.", "general_description": "Strict, highly disciplined top TN private college.",
        "exam_required": "TNEA", "cutoff": "198+/200", "average_package": "₹7.5 LPA"
    },
    {
        "n": "Amrita Univ", "lt": 10.9001, "ln": 76.9026,
        "category": "Private", "location": {"city": "Coimbatore", "state": "Tamil Nadu"},
        "weather": "Tropical.", "general_description": "Highly ranked in NIRF, strong research.",
        "exam_required": "AEEE / JEE Main", "cutoff": "Top 10%", "average_package": "₹7.1 LPA"
    },
    {
        "n": "SRM Institute", "lt": 12.8236, "ln": 80.0435,
        "category": "Private", "location": {"city": "Chennai", "state": "Tamil Nadu"},
        "weather": "Tropical.", "general_description": "Massive campus, huge IT recruiter drives.",
        "exam_required": "SRMJEEE", "cutoff": "Rank <10000", "average_package": "₹7.5 LPA"
    },
    {
        "n": "KIIT", "lt": 20.3533, "ln": 85.8164,
        "category": "Private", "location": {"city": "Bhubaneswar", "state": "Odisha"},
        "weather": "Hot and humid.", "general_description": "Large private university in eastern India.",
        "exam_required": "KIITEE", "cutoff": "Rank <5000", "average_package": "₹6.5 LPA"
    },
    {
        "n": "Nirma Univ", "lt": 23.1293, "ln": 72.5401,
        "category": "Private", "location": {"city": "Ahmedabad", "state": "Gujarat"},
        "weather": "Hot semi-arid.", "general_description": "Premier private college in Gujarat.",
        "exam_required": "JEE Main / GUJCET", "cutoff": "AIR <30000", "average_package": "₹8.0 LPA"
    },
    {
        "n": "MIT WPU", "lt": 18.5186, "ln": 73.8139,
        "category": "Private", "location": {"city": "Pune", "state": "Maharashtra"},
        "weather": "Pleasant.", "general_description": "Famous private college in Pune.",
        "exam_required": "MHT-CET / JEE Main", "cutoff": "95+ Percentile", "average_package": "₹7.0 LPA"
    },
    {
        "n": "SPIT", "lt": 19.1232, "ln": 72.8361,
        "category": "Private", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical.", "general_description": "Elite Mumbai college with top packages.",
        "exam_required": "MHT-CET", "cutoff": "99.5+ Percentile", "average_package": "₹15.0 LPA"
    },
    {
        "n": "DJSCE", "lt": 19.1077, "ln": 72.8373,
        "category": "Private", "location": {"city": "Mumbai", "state": "Maharashtra"},
        "weather": "Tropical.", "general_description": "Top choice for Mumbai students.",
        "exam_required": "MHT-CET", "cutoff": "99.0+ Percentile", "average_package": "₹10.0 LPA"
    },
    {
        "n": "CBIT", "lt": 17.3916, "ln": 78.3188,
        "category": "Private", "location": {"city": "Hyderabad", "state": "Telangana"},
        "weather": "Semi-arid.", "general_description": "Top EAMCET college in Telangana.",
        "exam_required": "TS EAMCET", "cutoff": "Rank <1500", "average_package": "₹8.5 LPA"
    },
    {
        "n": "LD College", "lt": 23.0336, "ln": 72.5463,
        "category": "Government", "location": {"city": "Ahmedabad", "state": "Gujarat"},
        "weather": "Semi-arid.", "general_description": "Gujarat's oldest engineering college.",
        "exam_required": "GUJCET", "cutoff": "Top 2%", "average_package": "₹6.0 LPA"
    },
    {
        "n": "SSN College", "lt": 12.7509, "ln": 80.1970,
        "category": "Private", "location": {"city": "Chennai", "state": "Tamil Nadu"},
        "weather": "Tropical.", "general_description": "Founded by Shiv Nadar, top TN private college.",
        "exam_required": "TNEA", "cutoff": "198+/200", "average_package": "₹8.0 LPA"
    },
    {
        "n": "Jamia Millia", "lt": 28.5616, "ln": 77.2802,
        "category": "Government", "location": {"city": "New Delhi", "state": "Delhi"},
        "weather": "Extreme seasons.", "general_description": "Very low fees, high ROI central university.",
        "exam_required": "JEE Main", "cutoff": "AIR <25000", "average_package": "₹9.0 LPA"
    },
    {
        "n": "AMU ZHCET", "lt": 27.9135, "ln": 78.0782,
        "category": "Government", "location": {"city": "Aligarh", "state": "Uttar Pradesh"},
        "weather": "Subtropical.", "general_description": "Historic university with strong core placements.",
        "exam_required": "AMUEEE", "cutoff": "Top 1%", "average_package": "₹6.5 LPA"
    },
    {
        "n": "Osmania Univ", "lt": 17.4128, "ln": 78.5262,
        "category": "Government", "location": {"city": "Hyderabad", "state": "Telangana"},
        "weather": "Semi-arid.", "general_description": "Top government college via EAMCET.",
        "exam_required": "TS EAMCET", "cutoff": "Rank <1000", "average_package": "₹7.5 LPA"
    }
]

# 2. Convert the list into a GeoJSON format dictionary
# GeoJSON is just a specific way of organizing dictionaries that map software understands.
geojson_features = {
    "type": "FeatureCollection",
    "features": []
}

for college in colleges_data:
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            # Warning: GeoJSON requires coordinates to be [Longitude, Latitude]
            "coordinates": [college["ln"], college["lt"]] 
        },
        "properties": {
            "name": college["n"],
            "category": college["category"],
            "location": f'{college["location"]["city"]}, {college["location"]["state"]}',
            "weather": college["weather"],
            "general_description": college["general_description"],
            "exam_required": college["exam_required"],
            "cutoff": college["cutoff"],
            "average_package": college["average_package"],
        }
    }
    geojson_features["features"].append(feature)

    # 4. Add the GeoJSON data as a map layer
# We also attach a simple hover tooltip so you can see the names
college_layer = folium.GeoJson(
    geojson_features,
    name="Colleges",
    tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["College:"]),
    popup=folium.GeoJsonPopup(
        fields=[
            "category",
            "location",
            "weather",
            "general_description",
            "exam_required",
            "cutoff",
            "average_package"
        ],
        aliases=[
            "Category:",
            "Location:",
            "Weather Condition:",
            "General Description:",
            "Required Exam:",
            "Cutoff:",
            "Average Package:"
        ],
        localize=True,
        labels=True
    )
).add_to(map)

search = folium.plugins.Search(
    layer=college_layer,
    geom_type="Point",
    placeholder="Search colleges...",
    collapsed=False,
    search_label="name",
    search_zoom=16
).add_to(map)

government = folium.FeatureGroup(name="Government Colleges",show = False)
private = folium.FeatureGroup(name="Private Colleges",show = False)

tropical = folium.FeatureGroup(name="Weather: Tropical",show = False)
semi = folium.FeatureGroup(name="Weather: Semi-arid",show = False)
hnh = folium.FeatureGroup(name="Weather: Hot and Humid",show = False)
hsa = folium.FeatureGroup(name="Weather: Hot Semi-arid",show = False)
sub = folium.FeatureGroup(name="Weather: Sub Tropical",show = False)
ple = folium.FeatureGroup(name="Weather: Pleasent",show = False)
ex = folium.FeatureGroup(name="Weather: Extreme Seasons",show = False)
tc = folium.FeatureGroup(name="Weather: Tropical Coastal",show = False)

for college in colleges_data:
    marker = folium.Marker(
        location=[college["lt"], college["ln"]],
        tooltip=college["n"],
        popup=folium.Popup(
            f"<b>{college['n']}</b>"
            f"<br>Category: {college['category']}</br>"
            f"<br>Location: {college['location']['city']}, {college['location']['state']}</br>"
            f"<br>Exam: {college['exam_required']}</br>"
            f"<br>Average package: {college['average_package']}</br>"
        )
    )
    if college["category"] == "Government":
        marker.add_to(government)
    elif college["category"] == "Private":
        marker.add_to(private)
        

    if college["weather"] == "Tropical.":
        marker.add_to(tropical)
    elif college["weather"]=="Semi-arid.":
        marker.add_to(semi)   
    elif college["weather"]=="Hot and humid.":
        marker.add_to(hnh) 
    elif college["weather"]=="Hot semi-arid.":
         marker.add_to(hsa)
    elif college["weather"]=="Subtropical.":
            marker.add_to(sub)  
    elif college["weather"]=="Pleasant.":
            marker.add_to(ple) 
    elif college["weather"]=="Extreme seasons.":
            marker.add_to(ex) 
    elif college["weather"]=="Tropical coastal.":
            marker.add_to(tc)  
    
tropical.add_to(map)
semi.add_to(map)
hnh.add_to(map)
hsa.add_to(map)
sub.add_to(map)
ple.add_to(map)
ex.add_to(map)
tc.add_to(map)

government.add_to(map)
private.add_to(map)




folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri WorldImagery",
    name="Satellite Map"
).add_to(map)

folium.TileLayer(
    tiles="https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
    attr="OpenTopoMap",
    name="Terrain Map"
).add_to(map)

folium.TileLayer("OpenStreetMap", name="Standard Map").add_to(map)


folium.LayerControl(position="topright", collapsed=True).add_to(map)
map.save("map.html")
map