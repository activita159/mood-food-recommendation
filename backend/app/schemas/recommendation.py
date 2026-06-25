from pydantic import BaseModel, Field
from typing import Optional


class RecommendationRequest(BaseModel):
    mood: str
    budget: str
    people_count: int = Field(..., gt=0)
    purpose: str
    category: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None


class RecommendationResult(BaseModel):
    id: int
    name: str
    category: str
    score: int
    rating: float
    price_min: int
    price_max: int
    budget_level: str
    distance_km: float
    reason: str
