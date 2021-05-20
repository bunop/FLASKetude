#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:55:35 2021

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

from flask_mongoengine import MongoEngine

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)
