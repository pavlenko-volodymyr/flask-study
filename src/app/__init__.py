# -*- coding: utf-8 -*-

__author__ = 'mindinpanic'

from flask import Flask


app = Flask(__name__)
from app import views
