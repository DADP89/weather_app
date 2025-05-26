import pytest
from weather.api import fetch_weather_data
import requests

class DummyResponse:
    def __init__(self, status_code: int, json_data: dict):
        self.status_code = status_code
        self._json = json_data
    
    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"Status {self.status_code}")
    
    def json(self):
        return self._json


def test_fetch_weather_data_success(monkeypatch):
    fake = {
        "location": {"name": "TestCity", "region": "T", "country": "X"},
        "current": {"last_updated": "2025-05-25 10:00", "temp_c": 20},
        "forecast": {"forecastday": [{"date": "2025-05-26", "astro": {}, "day": {}}]}
    }
    def fake_get(url, params):
        assert "key" in params and params["q"] == "TestCity"
        return DummyResponse(200, fake)

    monkeypatch.setattr(requests, "get", fake_get)
    data = fetch_weather_data(api_key="ABC", city_name="TestCity")
    assert data["location"]["name"] == "TestCity"
    assert data["current"]["temp_c"] == 20

def test_fetch_weather_data_http_error(monkeypatch):
    def fake_get(url, params):
        return DummyResponse(404, {})
    monkeypatch.setattr(requests, "get", fake_get)

    with pytest.raises(requests.HTTPError):
        fetch_weather_data(api_key="ABC", city_name="NoCity")