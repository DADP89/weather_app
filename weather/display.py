def print_weather_info(data):
    place = f"{data['location']['name']}, {data['location']['region']} - {data['location']['country']}"
    update = data["current"]["last_updated"]
    temp = data["current"]["temp_c"]
    feels = data["current"]["feelslike_c"]
    condition = data["current"]["condition"]["text"]
    wind = data["current"]["wind_kph"]
    humd = data["current"]["humidity"]
    uv = data["current"]["uv"]

    fc_day = data["forecast"]["forecastday"][0]
    fc_date = fc_day["date"]
    fc_sunrise = fc_day["astro"]["sunrise"]
    fc_sunset = fc_day["astro"]["sunset"]
    fc_data = fc_day["day"]
    fc_min_temp = fc_data["mintemp_c"]
    fc_max_temp = fc_data["maxtemp_c"]
    fc_avg_temp = fc_data["avgtemp_c"]
    fc_max_wind = fc_data["maxwind_kph"]
    fc_tot_prec = fc_data["totalprecip_mm"]
    fc_avg_humd = fc_data["avghumidity"]
    fc_cha_rain = fc_data["daily_chance_of_rain"]

    print(f"\n* WEATHER IN {place.upper()} (last updated: {update})")
    print(f"Temperature: {temp} °C -> Feels like: {feels} °C")
    print(f"Condition: {condition}")
    print(f"Wind: {wind} km/h")
    print(f"Humidity: {humd}%")
    print(f"UV: {uv}\n")
    print("-" * 85)
    print(f"\n* FORECAST -> {fc_date}")
    print(f"Sunrise: {fc_sunrise} | Sunset: {fc_sunset}")
    print(f"Temp. Min: {fc_min_temp}°C | Max: {fc_max_temp}°C | AVG: {fc_avg_temp}°C")
    print(f"Max Wind: {fc_max_wind} km/h | Precipitation: {fc_tot_prec} mm")
    print(f"AVG Humidity: {fc_avg_humd}% | Chance of rain: {fc_cha_rain}%")
    print()