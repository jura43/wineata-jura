from flask import Blueprint, redirect, render_template, request, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@auth.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')