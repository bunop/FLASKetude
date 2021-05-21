#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:06:11 2021

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

import unittest

from app import app
from database.db import db, initialize_db

app.config['MONGODB_SETTINGS']['host'] = 'mongodb://localhost/movie-bag-test'
initialize_db(app)


class BaseCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    def tearDown(self):
        # Delete Database collections after the test is complete
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
