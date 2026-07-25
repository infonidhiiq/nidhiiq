import sys
import os

# Add parent dir to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app.core.database import SessionLocal, engine, Base
from backend.app.models.models import PolicyProduct, LeadRequest, ClaimTicket, UserPolicy

def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    # Clear existing
    db.query(PolicyProduct).delete()
    db.query(UserPolicy).delete()
    db.query(ClaimTicket).delete()

    policies = [
        # 1. Term Life
        PolicyProduct(
            title="Click 2 Protect Super",
            provider_name="HDFC Life",
            provider_logo="hdfc_life",
            category="term_life",
            subcategory="1 Cr Term Plan",
            min_cover=5000000.0,
            max_cover=50000000.0,
            claim_settlement_ratio=99.5,
            network_hospitals_count=0,
            key_features="Return of Premium Option|Waiver of Premium on Disability|Instant Tax Benefit u/s 80C",
            base_monthly_premium=490.0,
            base_annual_premium=5880.0,
            tax_benefit="80C & 10(10D)",
            badge="Save up to 10% Online",
            popularity_score=99.5
        ),
        PolicyProduct(
            title="iProtect Smart Plan",
            provider_name="ICICI Prudential",
            provider_logo="icici_pru",
            category="term_life",
            subcategory="Term Life Insurance",
            min_cover=5000000.0,
            max_cover=100000000.0,
            claim_settlement_ratio=99.1,
            network_hospitals_count=0,
            key_features="Terminal Illness upfront payout|Accidental Cover up to 2 Cr|Special Female Discounts",
            base_monthly_premium=520.0,
            base_annual_premium=6240.0,
            tax_benefit="80C & 10(10D)",
            badge="PolicyBazaar Choice",
            popularity_score=98.0
        ),
        PolicyProduct(
            title="Smart Secure Plus",
            provider_name="Max Life",
            provider_logo="max_life",
            category="term_life",
            subcategory="1 Cr Cover Plan",
            min_cover=5000000.0,
            max_cover=50000000.0,
            claim_settlement_ratio=99.6,
            network_hospitals_count=0,
            key_features="24-hr Express Claim Settlement|Increasing cover option 5% yearly|Critical Illness Rider",
            base_monthly_premium=470.0,
            base_annual_premium=5640.0,
            tax_benefit="80C & 10(10D)",
            badge="Lowest Premium",
            popularity_score=99.0
        ),

        # 2. Health Insurance
        PolicyProduct(
            title="ReAssure 2.0 Titanium",
            provider_name="Niva Bupa Health",
            provider_logo="niva_bupa",
            category="health",
            subcategory="Family Floater & Individual",
            min_cover=500000.0,
            max_cover=10000000.0,
            claim_settlement_ratio=98.4,
            network_hospitals_count=10200,
            key_features="Unlimited ReAssure restore benefit|Lock-in premium till claim|Cashless in 30 mins",
            base_monthly_premium=650.0,
            base_annual_premium=7800.0,
            tax_benefit="Section 80D",
            badge="Unlimited Restore",
            popularity_score=99.0
        ),
        PolicyProduct(
            title="Optima Secure Health",
            provider_name="HDFC ERGO",
            provider_logo="hdfc_ergo",
            category="health",
            subcategory="Individual & Family",
            min_cover=1000000.0,
            max_cover=20000000.0,
            claim_settlement_ratio=99.2,
            network_hospitals_count=12500,
            key_features="4X Coverage Benefit|Zero non-medical deduction|Global Coverage optional",
            base_monthly_premium=890.0,
            base_annual_premium=10680.0,
            tax_benefit="Section 80D",
            badge="4X Cover Advantage",
            popularity_score=98.5
        ),
        PolicyProduct(
            title="Star Comprehensive Health",
            provider_name="Star Health",
            provider_logo="star_health",
            category="health",
            subcategory="Individual & Family",
            min_cover=500000.0,
            max_cover=5000000.0,
            claim_settlement_ratio=99.0,
            network_hospitals_count=14000,
            key_features="Air Ambulance Covered|No Capping on room rent|Free annual checkup for all",
            base_monthly_premium=610.0,
            base_annual_premium=7320.0,
            tax_benefit="Section 80D",
            badge="14,000+ Cashless Hospitals",
            popularity_score=97.5
        ),

        # 3. Investment & SIP
        PolicyProduct(
            title="NidhiIQ High Return Wealth SIP",
            provider_name="SBI Mutual Fund",
            provider_logo="sbi_mf",
            category="investment",
            subcategory="SIP / Wealth Creation",
            min_cover=500.0,
            max_cover=10000000.0,
            claim_settlement_ratio=100.0,
            network_hospitals_count=0,
            key_features="Invest ₹10k/mo & Get ₹1 Cr|15%+ Historical CAGR|0% Commission Direct Plan",
            base_monthly_premium=1000.0,
            base_annual_premium=12000.0,
            tax_benefit="Tax-Free 10(10D) & 80C",
            badge="Invest ₹10k Get ₹1 Cr",
            popularity_score=99.8
        ),
        PolicyProduct(
            title="Guaranteed Income Plan",
            provider_name="ICICI Prudential",
            provider_logo="icici_pru",
            category="investment",
            subcategory="Guaranteed Return Plan",
            min_cover=100000.0,
            max_cover=50000000.0,
            claim_settlement_ratio=99.1,
            network_hospitals_count=0,
            key_features="Lock in 7.5% Guaranteed Interest|Regular Annual Payouts|100% Capital Protection",
            base_monthly_premium=2500.0,
            base_annual_premium=30000.0,
            tax_benefit="Tax-Free Returns",
            badge="Guaranteed 7.5% Rate",
            popularity_score=98.0
        ),

        # 4. Motor & Car Insurance
        PolicyProduct(
            title="DriveProtect Comprehensive Car",
            provider_name="ICICI Lombard",
            provider_logo="icici_lombard",
            category="car",
            subcategory="Car Insurance",
            min_cover=100000.0,
            max_cover=5000000.0,
            claim_settlement_ratio=98.2,
            network_hospitals_count=9500, # Cashless garages
            key_features="Save up to 85%|Zero Depreciation Cover|Key & Lock Replacement|24x7 Roadside Assistance",
            base_monthly_premium=209.0,
            base_annual_premium=2499.0,
            tax_benefit="GST Input Claim",
            badge="Save up to 85%",
            popularity_score=99.0
        ),
        PolicyProduct(
            title="Motor Shield Car Insurance",
            provider_name="HDFC ERGO",
            provider_logo="hdfc_ergo",
            category="car",
            subcategory="Car Insurance",
            min_cover=100000.0,
            max_cover=5000000.0,
            claim_settlement_ratio=99.2,
            network_hospitals_count=11000,
            key_features="Instant Digital Policy|Overnight Garage Repairs|Engine Protector Rider",
            base_monthly_premium=230.0,
            base_annual_premium=2750.0,
            tax_benefit="GST Input Claim",
            badge="Instant Cashless Repair",
            popularity_score=97.0
        ),

        # 5. Two-Wheeler / Bike Insurance
        PolicyProduct(
            title="Express Bike Insurance",
            provider_name="Bajaj Allianz",
            provider_logo="bajaj_allianz",
            category="bike",
            subcategory="Two-Wheeler Insurance",
            min_cover=20000.0,
            max_cover=500000.0,
            claim_settlement_ratio=98.0,
            network_hospitals_count=6500,
            key_features="Starts @ ₹482/yr|Zero Inspection Required|Personal Accident Cover ₹15 Lakhs",
            base_monthly_premium=40.0,
            base_annual_premium=482.0,
            tax_benefit="GST Claim",
            badge="Starts @ ₹482/yr",
            popularity_score=98.5
        ),

        # 6. Child Savings & Education
        PolicyProduct(
            title="Child Education Future Plan",
            provider_name="Max Life",
            provider_logo="max_life",
            category="child",
            subcategory="Child Savings Plan",
            min_cover=500000.0,
            max_cover=20000000.0,
            claim_settlement_ratio=99.6,
            network_hospitals_count=0,
            key_features="Premium Waiver on Parent's Death|Milestone Payouts for College|Guaranteed Maturity Bonus",
            base_monthly_premium=1500.0,
            base_annual_premium=18000.0,
            tax_benefit="Section 80C & 10(10D)",
            badge="Secure Child's Future",
            popularity_score=96.0
        ),

        # 7. Pension & Retirement
        PolicyProduct(
            title="Golden Years Pension Annuity",
            provider_name="LIC of India",
            provider_logo="lic",
            category="pension",
            subcategory="Retirement Annuity",
            min_cover=1000000.0,
            max_cover=50000000.0,
            claim_settlement_ratio=98.7,
            network_hospitals_count=0,
            key_features="Guaranteed Pension for Life|Joint Life annuity option|Tax-free partial withdrawal",
            base_monthly_premium=2500.0,
            base_annual_premium=30000.0,
            tax_benefit="80CCC & 10(10A)",
            badge="Govt Backed Security",
            popularity_score=95.0
        ),

        # 8. Business & Group Health Insurance
        PolicyProduct(
            title="Employee Group Health Insurance",
            provider_name="Care Health",
            provider_logo="care_health",
            category="business",
            subcategory="Group Health Insurance",
            min_cover=100000.0,
            max_cover=1000000.0,
            claim_settlement_ratio=97.8,
            network_hospitals_count=11500,
            key_features="Save up to 65%|Zero Waiting Period for Pre-existing|Maternity & Newborn Covered",
            base_monthly_premium=350.0,
            base_annual_premium=4200.0,
            tax_benefit="Corporate Expense Claim",
            badge="Save up to 65%",
            popularity_score=97.0
        ),

        # 9. Family Office & HNI Wealth
        PolicyProduct(
            title="NidhiIQ HNI Family Office Suite",
            provider_name="NidhiIQ Advisory",
            provider_logo="nidhiiq_logo",
            category="family_office",
            subcategory="HNI Wealth & Real Estate",
            min_cover=50000000.0,
            max_cover=1000000000.0,
            claim_settlement_ratio=100.0,
            network_hospitals_count=0,
            key_features="Dedicated Wealth Manager|Curated Prime Commercial Real Estate|Estate & Estate Tax Structuring",
            base_monthly_premium=10000.0,
            base_annual_premium=120000.0,
            tax_benefit="Bespoke Structuring",
            badge="HNI Exclusive",
            popularity_score=100.0
        )
    ]

    for p in policies:
        db.add(p)

    # Seed User Active Policies
    user_pols = [
        UserPolicy(
            policy_number="PB-NIQ-HLT-9941",
            insured_name="Rahul Sharma",
            category="Health Insurance",
            provider_name="HDFC ERGO",
            sum_insured=1000000.0,
            premium_amount=10680.0,
            renewal_date="2027-04-12",
            status="Active"
        ),
        UserPolicy(
            policy_number="PB-NIQ-TRM-8812",
            insured_name="Rahul Sharma",
            category="Term Life Insurance",
            provider_name="HDFC Life",
            sum_insured=10000000.0,
            premium_amount=5880.0,
            renewal_date="2026-12-05",
            status="Active"
        )
    ]
    for up in user_pols:
        db.add(up)

    db.commit()
    print("Database successfully seeded with PolicyBazaar exact products!")

if __name__ == "__main__":
    seed_database()
