#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 17:39:42 2021

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

from .auth import SignupApi, LoginApi
from .movie import MoviesApi, MovieApi
from .reset_password import ForgotPassword, ResetPassword


def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')
