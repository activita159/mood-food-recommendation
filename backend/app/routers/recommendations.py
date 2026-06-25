from fastapi import APIRouter

from app.schemas.recommendation import RecommendationRequest
from app.services.recommendation_service import build_recommendations


router = APIRouter()


@router.post("")
def recommend_restaurants(request: RecommendationRequest):
    return {"data": build_recommendations(request)}
