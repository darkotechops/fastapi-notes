import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_login_and_create_note():
    email = f"{uuid.uuid4()}@test.com"
    password = "pass123"

    # register
    r = client.post("/auth/register", json={"email": email, "password": password})
    assert r.status_code == 200, r.text

    # login
    r = client.post("/auth/login", json={"email": email, "password": password})
    assert r.status_code == 200, r.text
    token = r.json()["access_token"]

    # create note
    r = client.post("/notes/", headers={"Authorization": f"Bearer {token}"}, json={"title":"t1","content":"b"})
    assert r.status_code == 200, r.text
    assert r.json()["title"] == "t1"

    # list notes
    r = client.get("/notes/", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200, r.text
    notes = r.json()
    assert isinstance(notes, list)
    assert any(n["title"] == "t1" for n in notes)
