from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prd.db"
app.config["SECRET_KEY"] = "9ee4d1c861b8046b3a7ec2b230d6bec5"
app.config["UPLOAD_FOLDER"] = "static/photos_posts"


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "home"

from matherest import routes