from flask import Flask, request, make_response
import os, json
from flask_cors import CORS, cross_origin
from weather_data import WeatherData

app = Flask(__name__)


@app.route("/")
def home():
    return "home page"


@app.route("/webhook", methods=["POST"])
@cross_origin()
def webhook():
    object = WeatherData()
    req = request.get_json(silent=True, force=True)
    print("Request")
    print(json.dumps(req))
    res = object.processRequest(req)
    res = json.dumps(res)
    print(res)
    r = make_response(res)
    r.headers["Content-Type"] = "application/json"
    return r


if __name__ == "__main__":
    
    
    app.run(host="127.0.0.1", port=5000)
