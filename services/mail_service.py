#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:36:46 2021

@author: Paolo Cozzi <paolo.cozzi@ibba.cnr.it>
"""

from threading import Thread
from flask_mail import Message

from resources.errors import InternalServerError

APP = None
MAIL = None


def initialize_mail_service(app, mail):
    global APP, MAIL

    APP = app
    MAIL = mail


def send_async_email(app, msg):
    with app.app_context():
        try:
            MAIL.send(msg)
        except ConnectionRefusedError:
            raise InternalServerError("[MAIL SERVER] not working")


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(APP, msg)).start()
