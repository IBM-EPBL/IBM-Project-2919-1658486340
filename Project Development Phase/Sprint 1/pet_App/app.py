from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from logging import Formatter, FileHandler
from forms import *


app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)


# Views and routes


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/contact')
def contact():
    return render_template('pages/placeholder.contact.html')


@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)


# Sql performances


def login_required(test):
    pass


# Run file
if __name__ == '__main__':
    app.run()
