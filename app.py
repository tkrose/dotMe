from flask import Flask, render_template
import requests
import json
import random

app = Flask(__name__)


@app.route("/")
def home():
    """
        Added a pageVars dictionary to hold any variables or items that
        you'd like to pass over to the template file (accessable from either template.html or the "extended" pages
        i.e. home.html and about.html)
    """
    pageVars = {
        "title": "Home"
    }
    return render_template("home.html", **pageVars)


@app.route("/about")
def about():
    """
        Added a pageVars dictionary to hold any variables or items that
        you'd like to pass over to the template file (accessable from either template.html or the "extended" pages
        i.e. home.html and about.html)
    """
    pageVars = {
        "title": "About"
    }
    return render_template("about.html", **pageVars)


@app.route("/getData")
def getData():
    response = requests.get('https://cat-fact.herokuapp.com/facts')
    print(response)
    #if response.status_code != 200:
        #raise ApiError('GET /tasks/ {}'.format[response.status_code])
    respObj = json.loads(response.text)
    text = respObj["all"][random.randint(0, 233)]["text"]
    return text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
