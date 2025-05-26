import argparse
from weather.api import fetch_weather_data
from weather.display import print_weather_info
from weather.config import load_api_key

def main():
    parser = argparse.ArgumentParser(description="Consulta el clima actual y el pronóstico de una ciudad.")
    parser.add_argument("city", help="Nombre de la ciudad a consultar (ej: Lima,PE)")
    args = parser.parse_args()
    
    try:
        api_key = load_api_key()
        data = fetch_weather_data(api_key=api_key, city_name=args.city)
        print_weather_info(data)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()