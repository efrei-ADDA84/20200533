from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if not lat or not lon:
        return jsonify({'error': 'Latitude and longitude parameters are required.'}), 400

    api_key = os.getenv('OPENWEATHER_API_KEY')  # Récupération de la clé API depuis les variables d'environnement

    if not api_key:
        return jsonify({'error': 'OpenWeather API key is missing.'}), 500

    # Appel à l'API OpenWeatherMap
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch weather data.'}), 500

    data = response.json()
    return jsonify({
            "city": data['name'],  
            "country": data['sys']['country'],  
            "weather_description": data['weather'][0]['description'],
            "temperature": data['main']['temp']
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)  # Exécution de l'application sur le port 8081
