from flask import render_template, url_for
from matherest import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/profile/<user>")
def profile(user):
    return render_template("profile.html", user=user)
