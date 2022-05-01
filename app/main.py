from fastapi import FastAPI

app = FastAPI(openapi_url=None)

@app.get("/settings")
def get_settings():
    return ""

@app.put("/settings")
def post_settings():
    return ""

