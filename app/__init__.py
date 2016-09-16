#author:PYsaber

from flask import Flask
from flask_mail import Mail
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)
mail = Mail(app)
from app import views
