#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 14:42:04 2021

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        "name": "The Shawshank Redemption",
        "casts": [
            "Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]


@app.route('/')
def hello():
    return {'hello': 'world'}


@app.route('/movies')
def movies():
    return jsonify(data)


@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    data.append(movie)
    return {'id': len(data)-1}, 200


@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie = request.get_json()
    data[index] = movie
    return jsonify(data[index]), 200


@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    data.pop(index)
    return 'None', 200


if __name__ == '__main__':
    app.run()
