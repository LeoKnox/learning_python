from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", login=False)

@app.route("/character")
def character():
    characterClass = [{"ClassId":"11", "Classes":"Fighter","Ability":"Sword"},
        {"ClassId":"22", "Classes":"Wizard","Ability":"Spell"}]
    print(characterClass)
    return render_template("character.html", characterClass=characterClass)

@app.route("/login")
def login():
    return render_template("login.html")