from config import API_KEY
from utils.fetch_weather import get_weather


def main():
    print("=== Simple Weather App ===")
    city = input("Enter a city name: ").strip()
    state = input("Enter the 2-letter state code (e.g., TX, GA): ").strip().upper()

    weather = get_weather(city, state, API_KEY)

    if weather:
        print(f"\nWeather in {weather['city']}, {weather['state']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Description: {weather['description']}")

    else:
        print("Could not fetch weather data. Please check the city name or your internet connection.")

if __name__ == "__main__":
    main()