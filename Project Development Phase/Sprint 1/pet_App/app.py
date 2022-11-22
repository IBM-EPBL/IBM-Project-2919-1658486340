from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import logging
from logging import Formatter, FileHandler
from flask_bcrypt import Bcrypt
from forms import *

# App
app = Flask(__name__)
app.app_context().push()
# Connect to the database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registration.db'
app.config['SECRET_KEY'] = '2ORwjMDy7f'
db = SQLAlchemy(app)


# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"

class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

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
    if form.validate():
        hashed_password = Bcrypt.generate_password_hash(form.password)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main'))
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)


# Run file
if __name__ == '__main__':
    app.run()
