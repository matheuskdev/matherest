from flask import render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user
from matherest import *
from matherest.forms import FormLogin, FormCreateAccount, FormPhoto
from matherest.models import User, Photo
import os
from werkzeug.utils import secure_filename


#Home and Login route
@app.route("/", methods=["GET", "POST"])
def home():
    form_login = FormLogin()

    if form_login.validate_on_submit():
        user = User.query.filter_by(
              email=form_login.email.data).first()
        if user and bcrypt.check_password_hash(user.password, 
                                       form_login.password.data):
            login_user(user)
            return redirect(url_for("profile", id_user=user.id))
    
    return render_template("home.html", form=form_login)



# Create Account route
@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    form_createaccount = FormCreateAccount()
    
    if form_createaccount.validate_on_submit():
        password = bcrypt.generate_password_hash(
                    form_createaccount.password.data)
        
        user = User(username=form_createaccount.username.data,
                    email=form_createaccount.email.data, 
                    password=password)
        
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True)
        return redirect(url_for("profile", id_user=user.id))
    return render_template("create_account.html", 
                           form=form_createaccount)



# Profile user route
@app.route("/profile/<id_user>", methods=["GET", "POST"])
@login_required
def profile(id_user):
    if int(id_user) == int(current_user.id):
        form_photo = FormPhoto()

        if form_photo.validate_on_submit():
            arquive = form_photo.photo.data
            secure_name = secure_filename(arquive.filename)

            arquive_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   app.config["UPLOAD_FOLDER"], secure_name)
            arquive.save(arquive_path)

            photo = Photo(image=secure_name, id_user=current_user.id)
            
            database.session.add(photo)
            database.session.commit()

        return render_template("profile.html", 
                               user=current_user, form=form_photo)
    else:
        user = User.query.get(int(id_user))
        return render_template("profile.html", user=user, form=None)



#Logout user rout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))