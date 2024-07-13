from time import time
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from apis.auth import authenticate_user, create_access_token, get_current_user
from schemas.token import Token

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect password")
    access_token = create_access_token(data={"sub": "admin"})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/")
async def root():
    with open("static/index.html", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(html)


@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': '1.0', "time": time()}


@app.get('/secure-ping')
async def secure_ping(current_user: dict = Depends(get_current_user)):
    return {'res': 'secure pong', 'version': '1.0', "time": time(), "user": current_user}


# Secure docs and redoc with authentication
@app.get("/docs", include_in_schema=False)
async def get_docs(current_user: dict = Depends(get_current_user)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/redoc", include_in_schema=False)
async def get_redoc(current_user: dict = Depends(get_current_user)):
    return get_redoc_html(openapi_url="/openapi.json", title="redoc")
