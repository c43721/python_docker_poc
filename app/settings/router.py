from fastapi import APIRouter, Depends

from settings import SettingsService

router = APIRouter(prefix="/settings")

@router.get("/")
def settings(settings: SettingsService = Depends()):
    return settings.get_settings()

@router.put("/")
def post_settings(new_settings: dict, settings: SettingsService = Depends()):
    settings.write_settings(new_settings)

    return new_settings