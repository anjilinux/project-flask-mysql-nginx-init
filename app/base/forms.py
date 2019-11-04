# -*- encoding: utf-8 -*-
"""
Flask Boilerplate Dashboard
Author: AppSeed.us - App Generator 
License: MIT
"""

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField

## login and registration


class LoginForm(FlaskForm):
    username = TextField('Username', id='username_login')
    password = PasswordField('Password', id='pwd_login')


class CreateAccountForm(FlaskForm):
    username = TextField('Username', id='username_create')
    email = TextField('Email')
    password = PasswordField('Password', id='pwd_create')
