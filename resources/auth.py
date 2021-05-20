#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 17:55:08 2021

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

import json
import datetime

from flask import Response, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from database.models import User


class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200


class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(
            identity=str(user.id),
            expires_delta=expires)

        return Response(
            json.dumps({'token': access_token}),
            mimetype="application/json",
            status=200)
