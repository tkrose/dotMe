from flask import Flask, render_template
import requests
import json

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
	if response.status_code != 200:
		raise ApiError('GET /tasks/ {}'.format[response.status_code])
	respObj = json.loads(response.text)
	print(respObj["all"][1])
	return dict(respObj["all"][1])

if __name__ == "__main__":
	app.run(debug=True)
