import json
from pathlib import Path
from typing import Optional

from app.schemas.recommendation import RecommendationRequest, RecommendationResult
from app.schemas.restaurant import MenuItem, Restaurant


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
RESTAURANTS_FILE = DATA_DIR / "restaurants.json"
MENUS_FILE = DATA_DIR / "menus.json"


def _read_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_restaurants() -> list[Restaurant]:
    return [Restaurant(**item) for item in _read_json(RESTAURANTS_FILE)]


def load_menus() -> list[MenuItem]:
    return [MenuItem(**item) for item in _read_json(MENUS_FILE)]


def get_restaurant_by_id(restaurant_id: int) -> Optional[Restaurant]:
    return next(
        (
            restaurant
            for restaurant in load_restaurants()
            if restaurant.id == restaurant_id
        ),
        None,
    )


def get_menus_by_restaurant_id(restaurant_id: int) -> list[MenuItem]:
    return [
        menu
        for menu in load_menus()
        if menu.restaurant_id == restaurant_id
    ]


def build_recommendations(
    request: RecommendationRequest,
) -> list[RecommendationResult]:
    results = []

    for restaurant in load_restaurants():
        score, reasons = _score_restaurant(request, restaurant)
        if score <= 0:
            continue

        results.append(
            RecommendationResult(
                id=restaurant.id,
                name=restaurant.name,
                category=restaurant.category,
                score=score,
                rating=restaurant.rating,
                price_min=restaurant.price_min,
                price_max=restaurant.price_max,
                budget_level=restaurant.budget_level,
                distance_km=restaurant.distance_km,
                reason=", ".join(reasons),
            )
        )

    return sorted(results, key=lambda item: item.score, reverse=True)


def _score_restaurant(
    request: RecommendationRequest,
    restaurant: Restaurant,
) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []

    if request.mood in restaurant.mood_tags:
        score += 30
        reasons.append(f"符合你的「{request.mood}」心情")

    if request.budget == restaurant.budget_level:
        score += 20
        reasons.append(f"預算等級符合「{request.budget}」")

    if request.purpose in restaurant.purpose_tags:
        score += 15
        reasons.append(f"適合「{request.purpose}」")

    if request.category and request.category == restaurant.category:
        score += 10
        reasons.append(f"餐廳類型符合「{request.category}」")

    if request.city and request.city == restaurant.city:
        score += 10
        reasons.append(f"位於「{request.city}」")

    if request.district and request.district == restaurant.district:
        score += 5
        reasons.append(f"地區符合「{request.district}」")

    if restaurant.distance_km <= 2:
        score += 10
        reasons.append("距離 2 公里內")

    if restaurant.rating >= 4.5:
        score += 5
        reasons.append("評分 4.5 以上")

    if not reasons:
        reasons.append("與部分條件相近")

    return score, reasons
