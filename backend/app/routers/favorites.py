from fastapi import APIRouter, Query

from app.schemas.favorite import FavoriteRequest
from app.schemas.restaurant import RestaurantSummary
from app.services.recommendation_service import get_restaurant_by_id


router = APIRouter()

_favorites: list[FavoriteRequest] = []


def _dump_model(model):
    if hasattr(model, "model_dump"):
        return model.model_dump()
    return model.dict()


@router.post("")
def add_favorite(request: FavoriteRequest):
    exists = any(
        favorite.user_id == request.user_id
        and favorite.restaurant_id == request.restaurant_id
        for favorite in _favorites
    )
    if not exists:
        _favorites.append(request)

    return {"data": request, "message": "Favorite saved"}


@router.get("")
def list_favorites(user_id: int = Query(..., gt=0)):
    restaurant_ids = [
        favorite.restaurant_id
        for favorite in _favorites
        if favorite.user_id == user_id
    ]
    restaurants = []
    for restaurant_id in restaurant_ids:
        restaurant = get_restaurant_by_id(restaurant_id)
        if restaurant is not None:
            restaurants.append(RestaurantSummary(**_dump_model(restaurant)))

    return {"data": restaurants}


@router.delete("/{restaurant_id}")
def delete_favorite(restaurant_id: int, user_id: int = Query(..., gt=0)):
    before_count = len(_favorites)
    _favorites[:] = [
        favorite
        for favorite in _favorites
        if not (
            favorite.user_id == user_id
            and favorite.restaurant_id == restaurant_id
        )
    ]

    return {
        "data": {
            "user_id": user_id,
            "restaurant_id": restaurant_id,
            "deleted": len(_favorites) < before_count,
        }
    }
