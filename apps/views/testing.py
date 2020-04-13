from apps import app
from flask import render_template,url_for
from flask import Blueprint

testing = Blueprint('login',__name__)

@testing.route('/',methods=['GET','POST'])
def index():
  return render_template('testing.html')