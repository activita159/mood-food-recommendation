from pydantic import BaseModel


class RestaurantSummary(BaseModel):
    id: int
    name: str
    category: str
    city: str
    district: str
    rating: float
    price_min: int
    price_max: int
    budget_level: str
    distance_km: float
    features: list[str]


class Restaurant(RestaurantSummary):
    mood_tags: list[str]
    purpose_tags: list[str]
    address: str
    description: str


class MenuItem(BaseModel):
    id: int
    restaurant_id: int
    name: str
    price: int
    tags: list[str]
    reason: str
