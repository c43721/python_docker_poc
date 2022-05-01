from fastapi import APIRouter

router = APIRouter(prefix="/settings")

@router.get("/")
def get_settings():
    return "Hello from settings"

@router.put("/")
def post_settings():
    return "Hello from settings"