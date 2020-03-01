from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", login=True)

@app.route("/character")
def character():
    return render_template("index.html", login=False)

@app.route("/login")
def login():
    return render_template("index.html", login=False)