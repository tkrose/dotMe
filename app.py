from flask import Flask, render_template
import requests
import json
import random

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/getData")
def getData():
    response = requests.get('https://cat-fact.herokuapp.com/facts')
    print(response)
    #if response.status_code != 200:
        #raise ApiError('GET /tasks/ {}'.format[response.status_code])
    respObj = json.loads(response.text)
    text = respObj["all"][random.randint(0, 233)]["text"]
    return text


@app.route("/printYML")
def printYML():
    f = open('requirements.yml', 'r')
    reqs = f.read()
    f.close()
    return reqs


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
