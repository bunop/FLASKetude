#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 14:42:04 2021

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

import os

from flask import Flask, request, Response
from dotenv import load_dotenv

from database.db import initialize_db
from database.models import Movie

app = Flask(__name__)

# take environment variables from .env
load_dotenv()

# http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag',
    'username': os.getenv('APP_USER'),
    'password': os.getenv('APP_PASS'),
    'authentication_source': 'admin'
}

# connect to database
initialize_db(app)


@app.route('/movies')
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)


@app.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {'id': str(id)}, 200


@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200


@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Movie.objects.get(id=id).delete()
    return '', 200


@app.route('/movies/<id>')
def get_movie(id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)


if __name__ == '__main__':
    app.run()
