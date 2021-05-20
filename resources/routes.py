#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 17:39:42 2021

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

from .auth import SignupApi, LoginApi
from .movie import MoviesApi, MovieApi


def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
