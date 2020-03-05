from application import app, db
from application.models import Character, Room, Dungeon
from flask import render_template, request, json, Response

characterClass = [{"ClassId":"11", "Classes":"Fighter","Ability":"Sword"},
    {"ClassId":"22", "Classes":"Wizard","Ability":"Spell"}]

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)

@app.route("/character/")
@app.route("/character/<cid>")
def character(cid="11"):
    return render_template("character.html", characterClass=characterClass, character=True, cid=cid)

@app.route("/selection", methods = ["GET", "POST"])
def selection():
    ClassId = request.form.get('ClassId')
    Classes = request.form.get('Classes')
    return render_template("select.html", data={"ClassId":ClassId, "Classes":Classes})

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/api")
@app.route("/api/<idx>")
def api(idx=None):
    if (idx == None):
        jdata = characterClass
    else:
        jdata = characterClass[int(idx)]

    return Response(json.dumps(jdata), mimetype="/application/json")

@app.route("/player")
def player():
    #Character(char_id=1, char_name="Xingu", char_class="Figther",atk=12,ac=11).save()
    #Character(char_id=2, char_name="Eveehi", char_class="Wizard",atk=12,ac=11).save()
    players = Character.objects.all()
    return render_template("player.html", players=players)