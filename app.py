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
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from dotenv import load_dotenv

from database.db import initialize_db
from resources.routes import initialize_routes
from resources.errors import errors
from services.mail_service import initialize_mail_service

# initialize stuff
app = Flask(__name__)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
mail = Mail()

# take environment variables from .env
load_dotenv()

# http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag',
    'username': os.getenv('APP_USER'),
    'password': os.getenv('APP_PASS'),
    'authentication_source': 'admin'
}

# https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage/
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')

# https://pythonhosted.org/Flask-Mail/#configuring-flask-mail
app.config["MAIL_SERVER"] = os.getenv('MAIL_SERVER')
app.config["MAIL_PORT"] = os.getenv("MAIL_PORT")
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

# registering blueprints
initialize_routes(api)

# initialize mail services
mail.init_app(app)
initialize_mail_service(app, mail)

if __name__ == '__main__':
    # connect to database
    initialize_db(app)

    app.run()
