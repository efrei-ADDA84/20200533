import os
import requests

def get_weather(latitude, longitude, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"La météo à la latitude {latitude} et longitude {longitude} est : {weather_description}, Température : {temperature} °C"
    else:
        return "Erreur lors de la récupération des données météorologiques"

if __name__ == "__main__":
    latitude = os.getenv("LAT")
    longitude = os.getenv("LONG")
    api_key = os.getenv("API_KEY")

    if latitude and longitude and api_key:
        print(get_weather(latitude, longitude, api_key))
    else:
        print("Veuillez fournir les variables d'environnement LAT, LONG et API_KEY.")
