from flask import Flask, \
render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/profile/<user>")
def profile(user):
    return render_template("profile.html", user=user)



if __name__ == "__main__":
    app.run(debug=True)