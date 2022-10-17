from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/home")
def home():
    return render_template("index.html")


@views.route("/about")
def about():
    return render_template("about.html")


@views.route("/signin")
def signin():
    return render_template("signin.html")


@views.route("/signup")
def signup():
    return render_template("signup.html")
