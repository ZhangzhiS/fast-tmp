from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt

from app.core.config import settings

ALGORITHM = "HS256"


def create_access_token(
        subject: Union[str, Any]
) -> str:
    """创建访问的token"""
    to_encode = {"exp": settings.TOKEN_EXP, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

