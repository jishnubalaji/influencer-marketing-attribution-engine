# Influencer Marketing ROI & Attribution Analytics Engine 🚀

An engineering-grade data analytics pipeline designed to model, simulate, and optimize multi-channel startup marketing budgets. This project processes relational database schemas and aggregates high-volume conversion attribution logs to calculate tier-based ROI and mitigate marketing spend leakage.

---

## 🛠️ Tech Stack & Architecture
* **Language/Environment:** Python 3.x (Pandas, Datetime) | Google Colab
* **Database Logic:** Relational SQL Schema (PostgreSQL Compliant)
* **Design Framework:** Many-to-Many Bridge Table Architecture with custom promo-code attribution logs.

---

## 📦 S – The Scope (The Business Problem)
Early-stage and scaling consumer startups often experience significant capital inefficiency due to unoptimized influencer marketing channels. This project builds a programmatic engine that processes **2,300+ unique user conversion logs** across 20 distinct creator profiles to determine exact customer acquisition metrics and isolate performance traps.

---

## 💻 I – The Infrastructure (Data Schema)
The underlying database engine relies on a 4-tier normalized relational database model:
1. `influencers`: Master data tracking creator tiers, niche alignment, and baseline costs.
2. `campaigns`: Macro tracking of quarterly marketing allocations and budgets.
3. `campaign_roster`: A strict many-to-many bridge table tying creators to campaigns via unique tracking promo codes (`custom_promo_code`).
4. `attribution_logs`: High-frequency transactional checkout data capturing gross order value and applied discounts.

---

## ⚙️ R – The Results (Executive Business Intelligence)
Running the aggregation matrix across the simulated transaction layer uncovered high-leverage allocation insights:

| Creator Tier | Total Spend (₹) | Total Revenue Generated (₹) | Total Conversions | Cost Per Acquisition (CPA) | Net Profit (₹) | ROI Percentage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Macro** | 41,488.08 | 429,637.77 | 212 | **₹195.70** | 388,149.69 | **935.57%** |
| **Micro** | 25,293.02 | 260,876.28 | 121 | **₹209.03** | 235,583.26 | **931.42%** |
| **Mega** | 659,777.95 | 4,051,495.19 | 2060 | **₹320.28** | 3,391,717.24 | **514.07%** |

### 🚨 Core Strategic Recommendations:
1. **The Mega Trap:** While Mega influencers drive massive raw transaction volume (₹40.5L), they suffer severe capital degradation, costing **₹320.28 per user acquisition** with a vastly lower efficiency metric (514% ROI).
2. **The Efficiency Scaling Sweet Spot:** Macro and Micro segments represent elite performance clusters, maintaining an average **~933% ROI** and a highly optimized baseline CPA (~₹202). 
3. **Execution Directive:** Recommend an immediate, systemic reallocation of 30% of upcoming marketing capital out of Mega contracts and directly into diversified Macro/Micro clusters to decrease aggregate CAC by ~37% and scale startup growth runway.
