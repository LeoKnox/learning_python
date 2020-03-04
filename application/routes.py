from application import app
from flask import render_template, request

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)

@app.route("/character/")
@app.route("/character/<cid>")
def character(cid="11"):
    characterClass = [{"ClassId":"11", "Classes":"Fighter","Ability":"Sword"},
        {"ClassId":"22", "Classes":"Wizard","Ability":"Spell"}]
    print(characterClass)
    return render_template("character.html", characterClass=characterClass, character=True, cid=cid)

@app.route("/selection", methods = ["GET", "POST"])
def selection():
    ClassId = request.form.get('ClassId')
    Classes = request.form.get('Classes')
    return render_template("select.html", data={"ClassId":ClassId, "Classes":Classes})

@app.route("/login")
def login():
    return render_template("login.html", login=True)