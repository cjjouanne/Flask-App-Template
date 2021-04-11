from my_app import app, bcrypt, db, mail, cache
from flask import render_template, jsonify, redirect, url_for
from my_app.models import User
from my_app.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user
from flask_mail import Message

@app.route('/')
@cache.cached(timeout=50)
def hello_world():
    return render_template('home.html')
