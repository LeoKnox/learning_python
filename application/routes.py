from application import app, db
from application.models import Character, Room, Dungeon
from flask import render_template, request, json, Response, redirect, flash
from application.forms import LoginForm, CharacterForm

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_name = form.charName.data
        login_class = form.charClass.data
        character = Character.objects(char_name = login_name).first()
        if character and login_class == character.char_class:
            flash(f"{character.char_name}, you are in!")
            return redirect("/index")
        else:
            flash("There be errerrerrors!")
    return render_template("login.html", title="Loggin' in", form=form, login=True)

@app.route("/api")
@app.route("/api/<idx>")
def api(idx=None):
    if (idx == None):
        jdata = characterClass
    else:
        jdata = characterClass[int(idx)]

    return Response(json.dumps(jdata), mimetype="/application/json")

@app.route("/player", methods=["GET","POST"])
def player():
    form = CharacterForm()
    if form.validate_on_submit():
    #players = Character.objects.all()
        char_id = Character.objects.count()
        char_id += 1

        char_name   = form.char_name.data
        char_class  = form.char_class.data
        atk         = form.atk.data
        ac          = form.ac.data

        character = Character(char_id=char_id, char_class=char_class, atk=atk, ac=ac)
        character.save()
        flash("Go adventure!")
        return redirect(url_for("index"))

    return render_template("player.html", form=form) # add menu create=True