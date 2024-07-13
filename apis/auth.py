from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from schemas.token import Token
from core.hashing import Hasher
from core.security import create_access_token
from core.config import settings

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

@router.post(
    "/token",
    response_model=Token,
    summary="Generate access token",
    description="Generates a JWT access token for the admin user.")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != settings.ADMIN_USERNAME:
        raise HTTPException(status_code=400, detail="Incorrect credentials")
    if not Hasher.verify_password(form_data.password, settings.ADMIN_PASSWORD_HASH):
        raise HTTPException(status_code=400, detail="Incorrect credentials")
    access_token, expire = create_access_token(data={"sub": settings.ADMIN_USERNAME})
    return {"access_token": access_token, "token_type": "bearer", "expire": expire.isoformat()}

async def get_current_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if payload.get("sub") is None:
            raise credentials_exception
    except JWTError as exc:
        raise credentials_exception from exc
    return token
