from requests.api import request
import uvicorn
from flask import Flask, request
import weather_api, timezone_api, translation_api, speech_recognition_api, pdf_api

app = Flask(__name__)


@app.route("/timezone", methods=["GET", "POST"])
def timezone():
    city_name = request.args.get("city_name")
    return timezone_api.time_zone(city_name)


@app.route("/weather",  methods=["GET", "POST"])
def weather():
    city_name = request.args.get("city_name")
    return weather_api.weather_by_city_name(city_name)


@app.route("/translate", methods=["GET", "POST"])
def translation():
    lang_from = request.args.get("lang_from")
    lang_to = request.args.get("lang_to")
    text = request.args.get("text")
    return translation_api.translate_text(lang_from, lang_to, text)


@app.route("/speech", methods=["GET", "POST"])
def speech():
    return str(speech_recognition_api.SpeakText())


@app.route("/pdf", methods=["GET", "POST"])
def pdf():
    pdf_name = request.args.get("pdf_name")
    return str(pdf_api.generate_pdf(pdf_name))

if __name__ == "__main__":
    app.run(debug=True)