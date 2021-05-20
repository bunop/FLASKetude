#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 17:55:08 2021

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

from flask import request
from database.models import User
from flask_restful import Resource


class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200
