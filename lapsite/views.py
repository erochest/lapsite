

from flask import (abort, flash, g, redirect, render_template, request,
                   session, url_for)

from lapsite import app


@app.route('/')
def index():
    return '<p>Hello LAP!</p>'

