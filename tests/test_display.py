import pytest
from weather.display import print_weather_info

@pytest.fixture
def minimal_data():
    return {
        "location": {"name": "Test", "region": "R", "country": "C"},
        "current": {
            "last_updated": "2025-05-25 12:00",
            "temp_c": 25,
            "feelslike_c": 27,
            "condition": {"text": "Sunny"},
            "wind_kph": 10,
            "humidity": 50,
            "uv": 5
        },
        "forecast": {
            "forecastday": [
                {
                    "date": "2025-05-26",
                    "astro": {"sunrise": "06:00 AM", "sunset": "06:00 PM"},
                    "day": {
                        "mintemp_c": 15,
                        "maxtemp_c": 30,
                        "avgtemp_c": 22.5,
                        "maxwind_kph": 12,
                        "totalprecip_mm": 0,
                        "avghumidity": 55,
                        "daily_chance_of_rain": 0
                    }
                }
            ]
        }
    }

def test_print_weather_info_contains_key_lines(capsys, minimal_data):
    print_weather_info(minimal_data)
    captured = capsys.readouterr().out
    assert "WEATHER IN TEST, R - C" in captured
    assert "Temperature: 25 °C -> Feels like: 27 °C" in captured
    assert "Sunrise: 06:00 AM" in captured
    assert "Chance of rain: 0%" in captured