# Will handle our database connection
# https://fastapi.tiangolo.com/tutorial/sql-databases/
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connection string. Specifies where is our SQL database located
# Format of a SQL string
# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:password@<ip-address/hostname>/database"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:@localhost/py_api"

# Engine is responsible for etablishing a connection for 
# SQLAlchemy to connect to postgres database.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# When you talk to a SQL database we need to make use of session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Models that represent table extend the Base class.
Base = declarative_base()

# Dependency
def get_db():
    # Gets a connection the db
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# Dependency
def get_db():
    # Gets a connection the db
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
