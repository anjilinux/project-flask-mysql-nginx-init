# -*- encoding: utf-8 -*-
"""
Flask Boilerplate Dashboard
Author: AppSeed.us - App Generator 
License: MIT
"""

from flask_migrate import Migrate
from os import environ
from sys import exit

from config import config_dict
from app import create_app, db

get_config_mode = environ.get('APPSEED_CONFIG_MODE', 'Debug')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid APPSEED_CONFIG_MODE environment variable entry.')

app = create_app(config_mode)
Migrate(app, db)
