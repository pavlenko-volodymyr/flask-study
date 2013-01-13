# -*- coding: utf-8 -*-

__author__ = 'mindinpanic'

from app import app


@app.route('/')
@app.route('/index')
def index():
    return u"Index page"
