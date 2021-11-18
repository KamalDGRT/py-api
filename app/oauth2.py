from jose import JWTError, jwt
from datetime import datetime, timedelta

# SECRET_KEY
# ALGORITHM
# EXPIRATION TIME OF THE TOKEN

SECRET_KEY = "bda873b79aa0a4bd34b50282a438e81f54f0fa8354b864021cfb22f02f4a08f9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
