import math
from typing import List, Dict, Any

class QuoteService:

    @staticmethod
    def calculate_term_life_quotes(age: int, gender: str, tobacco: bool, annual_income: float, sum_assured: float, policy_term: int) -> List[Dict[str, Any]]:
        # Base factor based on age
        base_rate_per_lakh = 45.0 + (max(0, age - 20) * 4.2)
        if tobacco:
            base_rate_per_lakh *= 1.6
        if gender == "female":
            base_rate_per_lakh *= 0.88 # female discount

        lakhs = sum_assured / 100000.0

        providers = [
            {
                "id": 1,
                "provider_name": "HDFC Life",
                "title": "Click 2 Protect Super",
                "logo": "hdfc_life",
                "claim_settlement_ratio": 99.5,
                "multiplier": 0.95,
                "badge": "Highest Claim Ratio",
                "features": ["Zero Cost Return of Premium at age 60", "Waiver of Premium on Critical Illness", "Instant Tax Benefit u/s 80C"],
                "riders": ["Critical Illness Cover (Rs 15 Lakh)", "Accidental Death Benefit (Rs 50 Lakh)"]
            },
            {
                "id": 2,
                "provider_name": "ICICI Prudential",
                "title": "iProtect Smart",
                "logo": "icici_pru",
                "claim_settlement_ratio": 99.1,
                "multiplier": 0.92,
                "badge": "NidhiIQ Top Pick",
                "features": ["Terminal Illness Payout upfront", "Special discounts for non-smokers", "Flexible Cover till age 85"],
                "riders": ["Accidental Cover", "Disability Rider"]
            },
            {
                "id": 3,
                "provider_name": "Max Life",
                "title": "Smart Secure Plus",
                "logo": "max_life",
                "claim_settlement_ratio": 99.6,
                "multiplier": 0.90,
                "badge": "Lowest Premium Guaranteed",
                "features": ["Special online discount up to 10%", "Increasing Cover 5% yearly", "Quick 24-hr Express Claim Settlement"],
                "riders": ["Critical Illness Benefit", "Hospital Cash Rider"]
            },
            {
                "id": 4,
                "provider_name": "TATA AIA",
                "title": "Sampoorna Raksha Supreme",
                "logo": "tata_aia",
                "claim_settlement_ratio": 99.0,
                "multiplier": 0.94,
                "badge": "Popular",
                "features": ["Life Stage Upgrade options", "Whole Life Cover up to age 100", "Tax Savings up to Rs 46,800/yr"],
                "riders": ["Accidental Death & Dismemberment"]
            }
        ]

        results = []
        for p in providers:
            annual_prem = round(base_rate_per_lakh * lakhs * p["multiplier"], 2)
            monthly_prem = round(annual_prem / 12.0, 2)
            results.append({
                "id": p["id"],
                "provider_name": p["provider_name"],
                "title": p["title"],
                "logo": p["logo"],
                "claim_settlement_ratio": p["claim_settlement_ratio"],
                "badge": p["badge"],
                "sum_assured": sum_assured,
                "policy_term": policy_term,
                "monthly_premium": monthly_prem,
                "annual_premium": annual_prem,
                "tax_savings_80c": round(annual_prem * 0.312, 2),
                "features": p["features"],
                "riders": p["riders"]
            })

        results.sort(key=lambda x: x["monthly_premium"])
        return results

    @staticmethod
    def calculate_health_quotes(age: int, cover_type: str, adults_count: int, children_count: int, sum_insured: float, city_tier: str, pre_existing_disease: bool) -> List[Dict[str, Any]]:
        lakhs = sum_insured / 100000.0
        base_prem = (6000.0 + (age * 120.0)) * (1.0 + (adults_count - 1) * 0.5 + children_count * 0.25)
        if pre_existing_disease:
            base_prem *= 1.25
        if city_tier == "tier1":
            base_prem *= 1.15

        providers = [
            {
                "id": 101,
                "provider_name": "Niva Bupa (Max Bupa)",
                "title": "ReAssure 2.0 Titanium",
                "network_hospitals": 10200,
                "claim_settlement_ratio": 98.4,
                "multiplier": 1.0,
                "badge": "Unlimited Restore Benefit",
                "features": ["Lock-in premium until claim", "3X sum insured boost", "No pre-policy medical checkup till age 50", "Cashless claim approval in 30 mins"]
            },
            {
                "id": 102,
                "provider_name": "Star Health",
                "title": "Comprehensive Health Insurance",
                "network_hospitals": 14000,
                "claim_settlement_ratio": 99.0,
                "multiplier": 0.95,
                "badge": "India's No. 1 Health Insurer",
                "features": ["Zero copay for all ages", "Air ambulance coverage up to Rs 5 Lakhs", "Annual free health checkups", "Bariatric surgery covered"]
            },
            {
                "id": 103,
                "provider_name": "HDFC ERGO",
                "title": "Optima Secure",
                "network_hospitals": 12500,
                "claim_settlement_ratio": 99.2,
                "multiplier": 1.08,
                "badge": "4X Coverage Advantage",
                "features": ["Secure Benefit doubles sum insured instantly", "Automatic Restore benefit", "Zero non-medical deduction", "Consumables covered in full"]
            },
            {
                "id": 104,
                "provider_name": "Care Health",
                "title": "Care Supreme Plan",
                "network_hospitals": 11500,
                "claim_settlement_ratio": 97.8,
                "multiplier": 0.88,
                "badge": "Best Value",
                "features": ["Cumulative Bonus Super up to 500%", "Unlimited automatic recharge", "Global coverage add-on available", "Daycare procedures 540+ covered"]
            }
        ]

        results = []
        for p in providers:
            annual_prem = round(base_prem * (lakhs / 10.0) * p["multiplier"], 2)
            monthly_prem = round(annual_prem / 12.0, 2)
            results.append({
                "id": p["id"],
                "provider_name": p["provider_name"],
                "title": p["title"],
                "network_hospitals": p["network_hospitals"],
                "claim_settlement_ratio": p["claim_settlement_ratio"],
                "badge": p["badge"],
                "sum_insured": sum_insured,
                "monthly_premium": monthly_prem,
                "annual_premium": annual_prem,
                "tax_savings_80d": round(min(75000.0, annual_prem * 0.312), 2),
                "features": p["features"]
            })

        results.sort(key=lambda x: x["monthly_premium"])
        return results

    @staticmethod
    def calculate_sip_projections(monthly_investment: float, tenure_years: int, expected_return_rate: float) -> Dict[str, Any]:
        i = (expected_return_rate / 100.0) / 12.0
        n = tenure_years * 12
        
        # Future value formula FV = P * [((1 + i)^n - 1) / i] * (1 + i)
        future_value = monthly_investment * (((math.pow(1 + i, n) - 1) / i)) * (1 + i)
        total_invested = monthly_investment * n
        estimated_returns = future_value - total_invested

        # Top Fund recommendations based on tenure/returns
        recommended_funds = [
            {
                "fund_name": "Parag Parikh Flexi Cap Fund",
                "category": "Flexi Cap",
                "cagr_3yr": "22.4%",
                "rating": "5 Star",
                "min_sip": 1000
            },
            {
                "fund_name": "Nippon India Small Cap Fund",
                "category": "Small Cap",
                "cagr_3yr": "31.2%",
                "rating": "5 Star",
                "min_sip": 500
            },
            {
                "fund_name": "SBI Bluechip Direct Fund",
                "category": "Large Cap",
                "cagr_3yr": "16.8%",
                "rating": "4 Star",
                "min_sip": 500
            },
            {
                "fund_name": "HDFC Mid-Cap Opportunities Fund",
                "category": "Mid Cap",
                "cagr_3yr": "24.6%",
                "rating": "5 Star",
                "min_sip": 1000
            }
        ]

        return {
            "monthly_investment": monthly_investment,
            "tenure_years": tenure_years,
            "expected_return_rate": expected_return_rate,
            "total_invested": round(total_invested, 2),
            "estimated_returns": round(estimated_returns, 2),
            "total_value": round(future_value, 2),
            "recommended_funds": recommended_funds
        }
