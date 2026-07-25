from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class PolicyProductSchema(BaseModel):
    id: int
    title: str
    provider_name: str
    provider_logo: Optional[str] = None
    category: str
    subcategory: Optional[str] = None
    min_cover: float
    max_cover: float
    claim_settlement_ratio: float
    network_hospitals_count: int
    key_features: Optional[str] = None
    base_monthly_premium: float
    base_annual_premium: float
    tax_benefit: str
    badge: Optional[str] = None
    popularity_score: float

    class Config:
        from_attributes = True

class TermLifeQuoteRequest(BaseModel):
    age: int = Field(..., ge=18, le=75)
    gender: str = "male" # male, female
    tobacco: bool = False
    annual_income: float = Field(1000000.0, ge=100000.0)
    sum_assured: float = Field(10000000.0, ge=2500000.0) # e.g. 1 Cr
    policy_term: int = Field(30, ge=5, le=50) # years

class HealthQuoteRequest(BaseModel):
    age: int = Field(..., ge=18, le=80)
    cover_type: str = "individual" # individual, family
    adults_count: int = 1
    children_count: int = 0
    sum_insured: float = Field(1000000.0, ge=300000.0) # e.g. 10 Lakhs or 1 Cr
    city_tier: str = "tier1" # tier1, tier2, tier3
    pre_existing_disease: bool = False

class MotorQuoteRequest(BaseModel):
    vehicle_type: str = "car" # car, bike
    reg_number: Optional[str] = "KA01MA1234"
    make_model: str = "Hyundai Creta"
    reg_year: int = 2022
    claims_made_last_year: bool = False
    cover_type: str = "comprehensive" # comprehensive, zero_dep, third_party

class SIPQuoteRequest(BaseModel):
    monthly_investment: float = Field(5000.0, ge=500.0)
    tenure_years: int = Field(15, ge=1, le=40)
    expected_return_rate: float = Field(12.0, ge=4.0, le=25.0)

class LeadCreateRequest(BaseModel):
    full_name: str
    phone_number: str
    email: Optional[str] = None
    interested_category: str
    preferred_time: Optional[str] = "Anytime"

class ClaimCreateRequest(BaseModel):
    insured_name: str
    policy_number: str
    phone_number: str
    category: str
    claim_amount: float
    hospital_or_incident: Optional[str] = None
