from my_app import app, bcrypt, db, cache
from flask import render_template, jsonify, redirect, url_for
from ..models import *
from ..forms import *
from flask_login import login_user, current_user, logout_user

@app.route('/')
@cache.cached(timeout=50)
def hello_world():
    return render_template('home.html')
