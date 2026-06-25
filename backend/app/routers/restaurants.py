from fastapi import APIRouter, HTTPException

from app.schemas.restaurant import MenuItem, Restaurant, RestaurantSummary
from app.services.recommendation_service import (
    get_menus_by_restaurant_id,
    get_restaurant_by_id,
    load_restaurants,
)


router = APIRouter()


def _dump_model(model):
    if hasattr(model, "model_dump"):
        return model.model_dump()
    return model.dict()


@router.get("")
def list_restaurants():
    restaurants = [
        RestaurantSummary(**_dump_model(restaurant))
        for restaurant in load_restaurants()
    ]
    return {"data": restaurants}


@router.get("/{restaurant_id}")
def get_restaurant(restaurant_id: int):
    restaurant = get_restaurant_by_id(restaurant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    return {"data": Restaurant(**_dump_model(restaurant))}


@router.get("/{restaurant_id}/menus")
def get_restaurant_menus(restaurant_id: int):
    restaurant = get_restaurant_by_id(restaurant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    menus = get_menus_by_restaurant_id(restaurant_id)
    if not menus:
        raise HTTPException(status_code=404, detail="Menus not found")

    return {"data": [MenuItem(**_dump_model(menu)) for menu in menus]}
