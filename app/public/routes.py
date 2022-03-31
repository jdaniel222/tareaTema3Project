from flask import render_template, request
from . import public
import app

@public.route('/')
def index():  # put application's code here
    return render_template('index.html')


