import json
from datetime import timedelta

from flask import Flask, render_template, request, url_for, jsonify, config, make_response, redirect
from flask_mysqldb import MySQL
from MySQLdb import escape_string
import bcrypt
import re
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, set_access_cookies, unset_jwt_cookies,
)

from app import home_view, login_view, signup_view

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_ACCESS_COOKIE_PATH'] = '/home'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)


app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

mysql = MySQL(app)
