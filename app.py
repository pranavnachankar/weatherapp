from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp', methods = ['GET', 'POST'])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
        # to get data from user in form, we are using request module
        'q' : request.form.get("city"),
        'appid' : request.form.get("appid"),
        'units' : request.form.get('units')
    }

    # now to get data from URL, we are using requests module
    response = requests.get(url, params=param)
    data = response.json()
    return f"data : {data}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)