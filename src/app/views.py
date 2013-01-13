# -*- coding: utf-8 -*-

__author__ = 'mindinpanic'


from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {
        'nickname': 'Vova'
    }
    posts = [
        {
            'author': {'nickname': 'Pechenushka'},
            'body': u'Моя красота неописуемая'
        },
        {
            'author': {'nickname': 'Vova'},
            'body': 'Some boring text'
        }
    ]
    return render_template(
        'index.html',
        title="Index",
        user=user,
        posts=posts
    )
