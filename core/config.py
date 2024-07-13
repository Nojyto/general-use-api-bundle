import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "General Use API Bundle"
    PROJECT_VERSION: str = "1.0.0"
    ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD_HASH: str = os.getenv("ADMIN_PASSWORD_HASH")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    TOKEN_EXPIRE_MINUTES: int = 30
    HIDE_DOCS: str = os.getenv("HIDE_DOCS", "False")
    OPENAPI_URL = "/openapi.json"
    DOCS_URL = "/docs"
    REDOC_URL = "/redoc"

settings = Settings()
