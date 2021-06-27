
from fastapi.routing import APIRouter
from app.models.schemas.foods import FoodInResponse
from app.models.domain.foods import Food
router = APIRouter()

@router.get(
    "/get-dummy",
    response_model=FoodInResponse,
    name="food:get-dummy-food",
)
async def get_dummy_food() -> FoodInResponse:
    dummy_food = Food(id = 22, name="bad_food_22")
    response = FoodInResponse(food = dummy_food)
    
    return response