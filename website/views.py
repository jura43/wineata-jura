from gettext import gettext
from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_babel import Babel, gettext

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/wineata')
def wineata():
    return render_template('wineata.html')

@views.route('/wineries')
def wineries():
    return render_template('wineries.html')

@views.route('/lang=<language>')
def set_language(language=None):
    session['lang'] = language
    return redirect(request.referrer)

