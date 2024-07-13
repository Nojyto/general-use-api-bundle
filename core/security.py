from datetime import datetime, timedelta, timezone
from typing import Optional, Tuple
from jose import jwt
from core.config import settings

def create_access_token(data: dict, exp_delta: Optional[timedelta] = None) -> Tuple[str, datetime]:
    to_encode = data.copy()
    if exp_delta:
        expire = datetime.now(timezone.utc) + exp_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt, expire
