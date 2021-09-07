from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
from flask_caching import Cache
import os

# Load environmet variables
load_dotenv('./env')

# Create app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")



#_______________________________________________________________________________
# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)
if db:
    print('DB IS READY!!!\n')

#_______________________________________________________________________________
# Cache config
cache = Cache(app, config={'CACHE_TYPE': 'redis',
                           'CACHE_REDIS_URL': 'redis://redis:6379/0'})
if cache:
    print('CACHE IS READY!!!\n')

#_______________________________________________________________________________
# Others
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from .routes import *
