from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from datetime import datetime
from backend.app.core.database import Base

class PolicyProduct(Base):
    __tablename__ = "policy_products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    provider_name = Column(String(100), nullable=False)
    provider_logo = Column(String(255), nullable=True)
    category = Column(String(50), nullable=False)  # term_life, health, motor, investment, pension, family_office
    subcategory = Column(String(100), nullable=True) # e.g. "Family Floater", "Super Topup", "1 Cr Term", "Zero Dep Car"
    min_cover = Column(Float, default=0.0) # in INR
    max_cover = Column(Float, default=0.0)
    claim_settlement_ratio = Column(Float, default=98.0) # e.g. 99.1%
    network_hospitals_count = Column(Integer, default=0) # e.g. 11000
    key_features = Column(Text, nullable=True) # pipe-separated features
    base_monthly_premium = Column(Float, nullable=False)
    base_annual_premium = Column(Float, nullable=False)
    tax_benefit = Column(String(50), default="80C & 10(10D)") # 80C, 80D
    badge = Column(String(50), nullable=True) # "Best Seller", "NidhiIQ Choice", "Lowest Premium"
    popularity_score = Column(Float, default=95.0)

class LeadRequest(Base):
    __tablename__ = "lead_requests"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    phone_number = Column(String(20), nullable=False)
    email = Column(String(150), nullable=True)
    interested_category = Column(String(50), nullable=False)
    preferred_time = Column(String(50), default="Anytime")
    status = Column(String(50), default="Pending") # Pending, Contacted, Closed
    created_at = Column(DateTime, default=datetime.utcnow)

class ClaimTicket(Base):
    __tablename__ = "claim_tickets"

    id = Column(Integer, primary_key=True, index=True)
    ticket_number = Column(String(50), unique=True, index=True)
    insured_name = Column(String(150), nullable=False)
    policy_number = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    category = Column(String(50), nullable=False)
    claim_amount = Column(Float, default=0.0)
    hospital_or_incident = Column(String(255), nullable=True)
    status = Column(String(50), default="Received") # Received, In Review, Approved, Disbursed
    created_at = Column(DateTime, default=datetime.utcnow)

class UserPolicy(Base):
    __tablename__ = "user_policies"

    id = Column(Integer, primary_key=True, index=True)
    policy_number = Column(String(100), unique=True, index=True)
    insured_name = Column(String(150), nullable=False)
    category = Column(String(50), nullable=False)
    provider_name = Column(String(100), nullable=False)
    sum_insured = Column(Float, nullable=False)
    premium_amount = Column(Float, nullable=False)
    renewal_date = Column(String(20), nullable=False)
    status = Column(String(50), default="Active")
