# This file will hold a bunch of utility functions
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    """
    Returns bcrypt hashed string
    """
    return pwd_context.hash(password)

# We could have done the below thing in the auth.py but we would have to
# import the above stuff again. So, it is better to group related stuff.

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
