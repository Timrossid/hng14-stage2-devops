from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import main

client = TestClient(main.app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_job(monkeypatch):
    fake_redis = MagicMock()
    monkeypatch.setattr(main, "r", fake_redis)

    response = client.post("/jobs")
    assert response.status_code == 200
    body = response.json()
    assert "job_id" in body
    fake_redis.lpush.assert_called_once()
    fake_redis.hset.assert_called_once()


def test_get_job_found(monkeypatch):
    fake_redis = MagicMock()
    fake_redis.hget.return_value = "completed"
    monkeypatch.setattr(main, "r", fake_redis)

    response = client.get("/jobs/test-job-id")
    assert response.status_code == 200
    assert response.json() == {"job_id": "test-job-id", "status": "completed"}


def test_get_job_not_found(monkeypatch):
    fake_redis = MagicMock()
    fake_redis.hget.return_value = None
    monkeypatch.setattr(main, "r", fake_redis)

    response = client.get("/jobs/missing-id")
    assert response.status_code == 200
    assert response.json() == {"error": "not found"}
