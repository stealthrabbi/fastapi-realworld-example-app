from fastapi import APIRouter

from app.api.routes import authentication, comments, profiles, tags, users, food
from app.api.routes.articles import api as articles

router = APIRouter()
router.include_router(authentication.router, tags=["authentication"], prefix="/users")
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(profiles.router, tags=["profiles"], prefix="/profiles")
router.include_router(articles.router, tags=["articles"])
router.include_router(
    food.router,
    tags=["food"],
    prefix="/food",
)
# router.include_router(articles.router, tags=["articles"])
router.include_router(tags.router, tags=["tags"], prefix="/tags")
