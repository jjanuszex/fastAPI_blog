from fastapi.testclient import TestClient
import pytest
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

@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():        
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield  TestClient(app)



def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "ser"}

def test_create_users(client):
    res = client.post(
        "/users/", json={"email": "test33@dupa.com", "password": "password123"})
    new_user = schemas.UserResponse(**res.json())
    assert res.status_code == 201
    assert new_user.email == "test33@dupa.com"