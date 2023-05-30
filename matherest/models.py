from matherest import database
from datetime import datetime

class User(database.Model):
    id =            database.Column(database.Integer, primary_key=True)
    username =      database.Column(database.String, nullable=False, unique=True)
    email =         database.Column(database.String, nullable=False, unique=True)
    password =      database.Column(database.String, nullable=False)
    photos =        database.relationship("Photo", backref="user", lazy=True)
    likes =         database.relationship("Like", backref="user", lazy=True)
    

class Photo(database.Model):
    id =            database.Column(database.Integer, primary_key=True)
    image =         database.Column(database.String, default="default.png")
    date_create =   database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_user =       database.Column(database.Integer,database.ForeignKey('user.id'), nullable=False)

class Like(database.Model):
    id =            database.Column(database.Integer, primary_key=True)
    id_user =       database.Column(database.Integer,database.ForeignKey('user.id'), nullable=False)
    id_photo =      database.Column(database.Integer,database.ForeignKey('photo.id'), nullable=False)
    