#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 14:42:04 2021

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from dotenv import load_dotenv

from database.db import initialize_db
from resources.routes import initialize_routes

# initialize stuff
app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

# take environment variables from .env
load_dotenv()

# http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag',
    'username': os.getenv('APP_USER'),
    'password': os.getenv('APP_PASS'),
    'authentication_source': 'admin'
}

# registering blueprints
initialize_routes(api)

# connect to database
initialize_db(app)

if __name__ == '__main__':
    app.run()
