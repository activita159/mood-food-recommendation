from pydantic import BaseModel, Field


class FavoriteRequest(BaseModel):
    user_id: int = Field(..., gt=0)
    restaurant_id: int = Field(..., gt=0)
