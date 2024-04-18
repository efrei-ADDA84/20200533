from flask import Flask, request, jsonify
import requests
import os
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST


app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Création d'un compteur pour le nombre de requêtes traitées
request_counter = Counter('requests_total', 'Total number of requests received')

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

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'contentType': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)  
