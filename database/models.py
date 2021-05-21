#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:56:10 2021

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

from flask_bcrypt import generate_password_hash, check_password_hash

from .db import db


class Movie(db.Document):
    name = db.StringField(required=True, unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
    added_by = db.ReferenceField('User')


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    movies = db.ListField(db.ReferenceField(
        'Movie', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


# register delete rule for added_by separately because User is not yet
# defined while defining Movie
User.register_delete_rule(Movie, 'added_by', db.CASCADE)
