-- ====================================================================
-- PROJECT: INFLUENCER MARKETING ROI ANALYSIS ENGINE
-- ARCHITECTURE: RELATIONAL DATABASE MODEL FOR PERFORMANCE TRACKING
-- ====================================================================

-- 1. INFLUENCERS MASTER TABLE
CREATE TABLE influencers (
    influencer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    niche VARCHAR(50) DEFAULT 'Tech/Business', -- e.g., Tech, Lifestyle, Finance
    tier VARCHAR(20) NOT NULL,                -- Nano, Micro, Macro, Mega
    follower_count INT NOT NULL,
    base_cost_per_post NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. CAMPAIGNS MASTER TABLE
CREATE TABLE campaigns (
    campaign_id SERIAL PRIMARY KEY,
    campaign_name VARCHAR(100) NOT NULL,
    target_audience VARCHAR(100),
    budget NUMERIC(12, 2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

-- 3. CAMPAIGN_ROSTER (BRIDGE TABLE MATCHING INFLUENCERS TO CAMPAIGNS)
CREATE TABLE campaign_roster (
    roster_id SERIAL PRIMARY KEY,
    campaign_id INT REFERENCES campaigns(campaign_id) ON DELETE CASCADE,
    influencer_id INT REFERENCES influencers(influencer_id) ON DELETE CASCADE,
    contract_cost NUMERIC(10, 2) NOT NULL,      -- Actual negotiated cost
    custom_promo_code VARCHAR(20) UNIQUE NOT NULL,
    allocated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. ATTRIBUTION LOGS (TRACKING EVERY CONVERSION/CONVERSION REVENUE)
CREATE TABLE attribution_logs (
    conversion_id SERIAL PRIMARY KEY,
    custom_promo_code VARCHAR(20) REFERENCES campaign_roster(custom_promo_code),
    customer_id INT NOT NULL,
    order_value NUMERIC(10, 2) NOT NULL,        -- Revenue brought in
    discount_applied NUMERIC(10, 2) DEFAULT 0.00,
    conversion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
