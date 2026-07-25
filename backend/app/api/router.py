from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import random

from backend.app.core.database import get_db
from backend.app.models.models import PolicyProduct, LeadRequest, ClaimTicket, UserPolicy
from backend.app.schemas.schemas import (
    PolicyProductSchema,
    TermLifeQuoteRequest,
    HealthQuoteRequest,
    SIPQuoteRequest,
    LeadCreateRequest,
    ClaimCreateRequest
)
from backend.app.services.quote_service import QuoteService

router = APIRouter()

@router.get("/health", tags=["Health"])
def health_check():
    return {"status": "online", "platform": "NidhiIQ PolicyBazaar Financial Engine"}

@router.get("/policies", response_model=List[PolicyProductSchema], tags=["Policies"])
def list_policies(
    category: Optional[str] = Query(None, description="Filter by category e.g. term_life, health, motor, investment"),
    search: Optional[str] = Query(None, description="Search term in title or provider name"),
    db: Session = Depends(get_db)
):
    query = db.query(PolicyProduct)
    if category:
        query = query.filter(PolicyProduct.category == category)
    if search:
        search_filter = f"%{search}%"
        query = query.filter(
            (PolicyProduct.title.like(search_filter)) | 
            (PolicyProduct.provider_name.like(search_filter))
        )
    return query.order_by(PolicyProduct.popularity_score.desc()).all()

@router.get("/policies/{policy_id}", response_model=PolicyProductSchema, tags=["Policies"])
def get_policy_detail(policy_id: int, db: Session = Depends(get_db)):
    policy = db.query(PolicyProduct).filter(PolicyProduct.id == policy_id).first()
    if not policy:
        raise HTTPException(status_code=404, detail="Policy product not found")
    return policy

@router.post("/quotes/term-life", tags=["Quote Calculators"])
def get_term_life_quotes(req: TermLifeQuoteRequest):
    return QuoteService.calculate_term_life_quotes(
        age=req.age,
        gender=req.gender,
        tobacco=req.tobacco,
        annual_income=req.annual_income,
        sum_assured=req.sum_assured,
        policy_term=req.policy_term
    )

@router.post("/quotes/health", tags=["Quote Calculators"])
def get_health_quotes(req: HealthQuoteRequest):
    return QuoteService.calculate_health_quotes(
        age=req.age,
        cover_type=req.cover_type,
        adults_count=req.adults_count,
        children_count=req.children_count,
        sum_insured=req.sum_insured,
        city_tier=req.city_tier,
        pre_existing_disease=req.pre_existing_disease
    )

@router.post("/quotes/sip", tags=["Quote Calculators"])
def calculate_sip(req: SIPQuoteRequest):
    return QuoteService.calculate_sip_projections(
        monthly_investment=req.monthly_investment,
        tenure_years=req.tenure_years,
        expected_return_rate=req.expected_return_rate
    )

@router.post("/leads/advisor-callback", tags=["Lead Generation"])
def submit_advisor_lead(req: LeadCreateRequest, db: Session = Depends(get_db)):
    lead = LeadRequest(
        full_name=req.full_name,
        phone_number=req.phone_number,
        email=req.email,
        interested_category=req.interested_category,
        preferred_time=req.preferred_time or "Anytime"
    )
    db.add(lead)
    db.commit()
    db.refresh(lead)
    return {
        "success": True,
        "message": "Callback request received! A certified NidhiIQ advisor will contact you shortly.",
        "lead_id": lead.id
    }

@router.post("/claims/submit", tags=["Claims Assistance"])
def submit_claim(req: ClaimCreateRequest, db: Session = Depends(get_db)):
    ticket_num = f"NIQ-CLM-{random.randint(100000, 999999)}"
    ticket = ClaimTicket(
        ticket_number=ticket_num,
        insured_name=req.insured_name,
        policy_number=req.policy_number,
        phone_number=req.phone_number,
        category=req.category,
        claim_amount=req.claim_amount,
        hospital_or_incident=req.hospital_or_incident,
        status="Received"
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return {
        "success": True,
        "ticket_number": ticket_num,
        "message": f"Claim ticket {ticket_num} registered successfully. Our 24x7 Claims Officer has been assigned."
    }

@router.get("/claims/track/{ticket_number}", tags=["Claims Assistance"])
def track_claim(ticket_number: str, db: Session = Depends(get_db)):
    ticket = db.query(ClaimTicket).filter(ClaimTicket.ticket_number == ticket_number).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Claim ticket not found")
    return {
        "ticket_number": ticket.ticket_number,
        "insured_name": ticket.insured_name,
        "policy_number": ticket.policy_number,
        "category": ticket.category,
        "claim_amount": ticket.claim_amount,
        "status": ticket.status,
        "created_at": ticket.created_at.strftime("%d %b %Y, %I:%M %p")
    }

@router.get("/user/policies", tags=["User Vault"])
def get_user_policies(db: Session = Depends(get_db)):
    policies = db.query(UserPolicy).all()
    total_tax_saved = sum([p.premium_amount * 0.312 for p in policies])
    return {
        "user_name": "Rahul Sharma",
        "policies": [
            {
                "policy_number": p.policy_number,
                "insured_name": p.insured_name,
                "category": p.category,
                "provider_name": p.provider_name,
                "sum_insured": p.sum_insured,
                "premium_amount": p.premium_amount,
                "renewal_date": p.renewal_date,
                "status": p.status
            } for p in policies
        ],
        "total_active_policies": len(policies),
        "estimated_tax_savings": round(total_tax_saved, 2)
    }
