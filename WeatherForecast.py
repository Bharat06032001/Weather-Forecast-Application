import requests

def get_weather_data(city):
    api_key = "1c5a260ee910cd5773565beb1bf5ca45"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None

def display_weather_data(data):
    if data:
        city = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_condition = data["weather"][0]["description"]
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Condition: {weather_condition}")
    else:
        print("No weather data available.")

def main():
    print("Welcome to the Weather Forecast Application!")
    city = input("Enter the name of the city: ")
    
    # Fetch weather data
    weather_data = get_weather_data(city)
    
    # Display weather data
    display_weather_data(weather_data)


main()
