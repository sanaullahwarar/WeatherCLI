import requests
from config import API_KEY
import datetime

def get_weather(city="Badin"):
    """Fetch current weather data for Badin from OpenWeatherMap API."""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print("\n🌦️  Live Weather Report")
            print(f"📍 City: {data['name']}, {data['sys']['country']}")
            print(f"🕒 Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"🌡️ Temperature: {data['main']['temp']}°C")
            print(f"🤔 Feels Like: {data['main']['feels_like']}°C")
            print(f"🌤️ Weather: {data['weather'][0]['description'].title()}")
            print(f"💧 Humidity: {data['main']['humidity']}%")
            print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        else:
            print("\n❌ Unable to fetch weather data. Please check your API key or city name.")
    except Exception as e:
        print("⚠️ Error occurred:", e)

def main():
    print("=== 🌦️ Weather CLI App (Badin City) ===")
    get_weather("Badin")

if __name__ == "__main__":
    main()
