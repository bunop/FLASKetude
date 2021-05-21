#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:38:04 2021

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

import json
import unittest

from app import app
from database.db import db, initialize_db

app.config['MONGODB_SETTINGS']['host'] = 'mongodb://localhost/movie-bag-test'
initialize_db(app)


class SignupTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    def test_successful_signup(self):
        # Given
        payload = json.dumps({
            "email": "paurakh011@gmail.com",
            "password": "mycoolpassword"
        })

        # When
        response = self.app.post(
            '/api/auth/signup',
            headers={"Content-Type": "application/json"},
            data=payload)

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        # Delete Database collections after the test is complete
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
