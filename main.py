from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/talia")
def talia():
	return "Hello, Talia!"

if __name__ == "__main__":
	app.run(debug=True)
