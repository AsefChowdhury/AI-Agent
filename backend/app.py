from flask import Flask, render_template, request

app = Flask(__name__)

# GET = Get data, POST = send data

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/handle_post", methods = ['POST'])
def handlePost():
    data = request.json;
    print(data)
    return{
        "note" : data["note"]
    }
        