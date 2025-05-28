from flask import Flask, request, render_template
from weather.api import fetch_weather_data
from weather.config import load_api_key

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None
    
    if request.method == "POST":
        city = request.form.get("city")
        try:
            api_key = load_api_key()
            weather_data = fetch_weather_data(api_key, city)
        except Exception as e:
            error = str(e)
    
    return render_template("index.html", weather=weather_data, error=error)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)