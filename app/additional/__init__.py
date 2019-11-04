# -*- encoding: utf-8 -*-
"""
Flask Boilerplate Dashboard
Author: AppSeed.us - App Generator 
License: MIT
"""

from flask import Blueprint

blueprint = Blueprint(
    'additional_blueprint',
    __name__,
    url_prefix='/additional',
    template_folder='templates',
    static_folder='static'
)
