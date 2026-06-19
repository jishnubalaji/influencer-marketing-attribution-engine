import pandas as pd
import random
from datetime import datetime, timedelta

# Set seed for reproducible data generation
random.seed(42)

# ====================================================================
# 1. GENERATE INFLUENCERS DATA
# ====================================================================
niches = ['Tech/Business', 'Lifestyle', 'Finance', 'Fitness']
tiers = ['Micro', 'Macro', 'Mega']
influencer_pool = []

for i in range(1, 21):
    tier = random.choice(tiers)
    if tier == 'Micro':
        followers = random.randint(10000, 100000)
    elif tier == 'Macro':
        followers = random.randint(100001, 500000)
    else:
        followers = random.randint(500001, 2000000)
        
    # Standardizing cost based on a real market proxy (approx 0.05 rupees/cents per follower baseline)
    base_cost = (followers * 0.05) + random.randint(50, 200)
    
    influencer_pool.append({
        "influencer_id": i,
        "name": f"Creator_{i}",
        "niche": random.choice(niches),
        "tier": tier,
        "follower_count": followers,
        "base_cost_per_post": round(base_cost, 2)
    })

df_influencers = pd.DataFrame(influencer_pool)

# ====================================================================
# 2. GENERATE CAMPAIGNS DATA
# ====================================================================
campaign_data = [
    {"campaign_id": 101, "campaign_name": "Q1_Tech_Launch", "target_audience": "Developers/Engineers", "budget": 150000.00},
    {"campaign_id": 102, "campaign_name": "Summer_Fitness_Push", "target_audience": "Gym Enthusiasts", "budget": 200000.00},
    {"campaign_id": 103, "campaign_name": "Financially_Fit_2026", "target_audience": "Young Professionals", "budget": 250000.00}
]
df_campaigns = pd.DataFrame(campaign_data)

# ====================================================================
# 3. GENERATE CAMPAIGN ROSTER (BRIDGE TABLE)
# ====================================================================
roster_pool = []
roster_id = 1

# Distribute influencers across the 3 campaigns based on their niche alignment
for idx, row in df_influencers.iterrows():
    # Assign to matching or random campaigns
    assigned_campaigns = [101] if row['niche'] == 'Tech/Business' else [102] if row['niche'] == 'Fitness' else [103] if row['niche'] == 'Finance' else [101, 102, 103]
    
    for c_id in assigned_campaigns:
        if random.random() > 0.3:  # 70% chance of allocation to create realistic variance
            # Negotiated cost might vary slightly from base cost
            contract_cost = row['base_cost_per_post'] * random.uniform(0.9, 1.1)
            promo_code = f"SRC_{row['name'].upper()}_{c_id}"
            
            roster_pool.append({
                "roster_id": roster_id,
                "campaign_id": c_id,
                "influencer_id": row['influencer_id'],
                "contract_cost": round(contract_cost, 2),
                "custom_promo_code": promo_code
            })
            roster_id += 1

df_roster = pd.DataFrame(roster_pool)

# ====================================================================
# 4. GENERATE ATTRIBUTION LOGS (CONVERSIONS & REVENUE)
# ====================================================================
attribution_pool = []
conversion_id = 1

# Generate simulated purchase logs for each active promo code
for idx, row in df_roster.iterrows():
    # Determine conversion volume based on influencer scale/tier
    inf_tier = df_influencers[df_influencers['influencer_id'] == row['influencer_id']]['tier'].values[0]
    num_conversions = random.randint(5, 20) if inf_tier == 'Micro' else random.randint(20, 80) if inf_tier == 'Macro' else random.randint(100, 350)
    
    for _ in range(num_conversions):
        # Scale order values to resemble standard checkout baskets
        order_value = random.uniform(500, 3500)
        discount = order_value * 0.10  # 10% off via promo code
        
        attribution_pool.append({
            "conversion_id": conversion_id,
            "custom_promo_code": row['custom_promo_code'],
            "customer_id": random.randint(10000, 99999),
            "order_value": round(order_value, 2),
            "discount_applied": round(discount, 2)
        })
        conversion_id += 1

df_attribution = pd.DataFrame(attribution_pool)

# ====================================================================
# VERIFICATION SUITE
# ====================================================================
print("🚀 SYSTEM DATA GENERATION COMPLETE 🚀\n")
print(f"Total Influencers Synced: {len(df_influencers)}")
print(f"Total Campaign Links Active: {len(df_roster)}")
print(f"Total Conversion Logs Tracked: {len(df_attribution)}\n")
print("=== ROSTER PREVIEW ===")
print(df_roster.head())
