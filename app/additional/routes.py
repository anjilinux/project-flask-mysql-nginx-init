# -*- encoding: utf-8 -*-
"""
Flask Boilerplate Dashboard
Author: AppSeed.us - App Generator 
License: MIT
"""

from app.additional import blueprint
from flask import render_template
from flask_login import login_required


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')
