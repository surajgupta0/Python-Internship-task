from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your OpenWeatherMap API key
API_KEY = "77fd7d112a8ddc1fc9bd009f909788bf"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            try:
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    weather_data = {
                        "city": data["name"],
                        "temperature": data["main"]["temp"],
                        "humidity": data["main"]["humidity"],
                        "condition": data["weather"][0]["description"].capitalize(),
                    }
                else:
                    error_message = f"City '{city}' not found. Please try again."
            except Exception as e:
                error_message = "Unable to fetch weather data. Please try again later."
        else:
            error_message = "Please enter a city name."

    return render_template("index.html", weather_data=weather_data, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
