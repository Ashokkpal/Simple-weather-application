from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Your OpenWeatherMap API key
API_KEY = 'your_openweather_api_key_here'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City not provided!"}), 400

    # Build the complete URL to fetch data from OpenWeatherMap
    complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

    # Get the weather data from OpenWeatherMap
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        weather_data = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"]
        }
        return jsonify(weather_data)
    else:
        return jsonify({"error": "City not found!"}), 404

if __name__ == '__main__':
    app.run(debug=True)
