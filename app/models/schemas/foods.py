from pydantic import BaseModel

from app.models.domain.foods import Food


class FoodInResponse(BaseModel):
    food: Food