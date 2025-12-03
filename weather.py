import requests

def get_weather(city):
    API_KEY = "004b1ff5f3cf79d3feeeb6fcf428d854" 
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        print("\n------ Weather Report ------")
        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {description}")
        print(f"Humidity: {humidity}%")
        print("----------------------------\n")

    else:
        print("\nCity not found. Please try again.\n")


if __name__ == "__main__":
    print("=== WEATHER APP ===")
    city = input("Enter city name: ")
    get_weather(city)
