from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms .validators import DataRequired

class LoginForm(FlaskForm):
    charName    =   StringField("Character Name", validators = [DataRequired()])
    charClass   =   StringField("Character Class", validators = [DataRequired()])
    rememberMe  =   BooleanField("Remember Me")
    submit      =   SubmitField("Login")

class CharacterForm(FlaskForm):
    char_name   =   StringField("Character Name", validators = [DataRequired()])
    char_class  =   StringField("Character Class", validators = [DataRequired()])
    atk         =   StringField("Attack", validators = [DataRequired()])
    ascii       =   StringField("Armor Class", validators = [DataRequired()])
    submit      =   SubmitField("Login")