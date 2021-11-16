# This file will hold a bunch of utility functions
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    """
    Returns bcrypt hashed string
    """
    return pwd_context.hash(password)
