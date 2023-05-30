from matherest import database, app
from matherest.models import User, Photo, Like
with app.app_context():
    database.create_all()