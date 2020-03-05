from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms .validators import DataRequired, Length, EqualTo
from application.models import Character

class LoginForm(FlaskForm):
    charName    =   StringField("Character Name", validators = [Length(min=3,max=25), DataRequired()])
    charClass   =   StringField("Character Class", validators = [DataRequired()])
    rememberMe  =   BooleanField("Remember Me")
    submit      =   SubmitField("Login")

class CharacterForm(FlaskForm):
    char_name   =   StringField("Character Name", validators = [Length(min=3,max=25), DataRequired()])
    char_class  =   StringField("Character Class", validators = [DataRequired()])
    atk         =   StringField("Attack", validators = [DataRequired()])
    ac          =   StringField("Armor Class", validators = [DataRequired()])
    submit      =   SubmitField("Login")

    def validate_char_name(self,char_name):
        character = Character.objects(char_name=char_name.data).first()
        if character:
            raise ValidationError("Name exists go forth and choose another.")