from fastapi.testclient import TestClient
from app.main import app
from app import schemas
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.database import get_db
from app.database import Base

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


# Step 1: Set up a local PostgreSQL database for testing.
# This command creates a new PostgreSQL database named "test_db" on your local machine.
# You might need to replace "your_username" with your actual PostgreSQL username.


# Step 2: Update your test configuration to use the URL of your local PostgreSQL database.
# Replace "your_username" and "your_password" with your actual PostgreSQL username and password.
SQLALCHEMY_DATABASE_URL = "postgresql://your_username:your_password@localhost/test_db"


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "ser"}

def test_create_users():
    res = client.post(
        "/users/", json={"email": "test2@dupa.com", "password": "password123"})
    new_user = schemas.UserResponse(**res.json())
    assert res.status_code == 201
    assert new_user.email == "test2@dupa.com"