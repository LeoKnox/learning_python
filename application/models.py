import flask
from application import db

class Character(db.Document):
    char_id     =   db.StringField( unique=True )
    char_name   =   db.StringField( max_length=50, unique=True )
    char_class  =   db.StringField( max_length=20 )
    atk         =   db.IntField( )
    ac          =   db.IntField( )

class Room(db.Document):
    classId     =   db.StringField( unique=True )
    length      =   db.IntField()
    width       =   db.IntField()
    wall        =   db.StringField( max_length=20 )

class Dungeon(db.Document):
    char_id     = db.StringField()
    classId     = db.StringField()