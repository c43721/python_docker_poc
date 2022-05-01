from json import load, dumps, JSONDecodeError
from fastapi import APIRouter

router = APIRouter(prefix="/settings")

def get_settings():
    """
        Returns the settings.json file as a dict
        Will return an empty dict if the file is not found, or if the json was invalid
    """
    
    try:
        with open('settings.json', 'r') as f:
            return load(f)
    except FileNotFoundError:
        return dict()
    except JSONDecodeError:
        return dict()

def write_settings(new_settings: dict):
    """
        Writes the new settings to the settings.json file   
    """

    # TODO: Resiliance with JSON structure (probably ensure that all callers enforce strict JSON structure) 
    with open('settings.json', 'w') as f:
        f.write(dumps(new_settings))

@router.get("/")
def settings():
    return get_settings()

@router.put("/")
def post_settings(settings: dict):
    write_settings(settings)

    return settings