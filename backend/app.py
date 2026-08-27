from flask import Flask, render_template, request
import requests

app = Flask(__name__)


# GET = Get data, POST = send data

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/handle_post", methods = ['POST'])
def handlePost():
    data = request.json;

    payload = {
                'model' : 'mistral',
               'prompt' : data["note"],
               'stream' : False}
    url = "http://localhost:11434/api/generate"

    response = requests.post(url, json=payload)

    return response.json();


if __name__ == "__main__":
    app.run(debug=True)