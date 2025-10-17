

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "1ef925623ec4ed663bc3300f168fbb1a"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    city = request.form.get("city")

    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url).json()

        if res.get("cod") == 200:
            weather = {
                "city": res["name"],
                "temp": res["main"]["temp"],
                "desc": res["weather"][0]["description"].title(),
                "humidity": res["main"]["humidity"]
            }
        else:
            weather = {"error": "City not found!"}

    return render_template("weatherapp.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
