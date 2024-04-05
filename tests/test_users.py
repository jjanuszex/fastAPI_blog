from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


# Step 1: Set up a local PostgreSQL database for testing.
# This command creates a new PostgreSQL database named "test_db" on your local machine.
# You might need to replace "your_username" with your actual PostgreSQL username.
createdb -U your_username test_db

# Step 2: Update your test configuration to use the URL of your local PostgreSQL database.
# Replace "your_username" and "your_password" with your actual PostgreSQL username and password.
SQLALCHEMY_DATABASE_URL = "postgresql://your_username:your_password@localhost/test_db"


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "ser"}

def test_create_users():
    response = client.post("/users/", json={"email": "janusz@gmail.com", "password": "password"})
    assert response.status_code == 201
    assert response.json() == []