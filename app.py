from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to Wholly Roasters!"


@app.route("/about", methods=["GET"])
def about():
    return "This is the 'About Us' page."