from flask import render_template, url_for
from matherest import app
from flask_login import login_required
from matherest.forms import FormLogin, FormCreateAccount


@app.route("/", methods=["GET", "POST"])
def home():
    formlogin = FormLogin()
    return render_template("home.html", form=formlogin)

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    formcreateaccount = FormCreateAccount()
    return render_template("create_account.html", form=formcreateaccount)


@app.route("/profile/<user>")
@login_required
def profile(user):
    return render_template("profile.html", user=user)
