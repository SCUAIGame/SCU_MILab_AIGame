#coding=utf-8
from flask import render_template, flash, redirect
from app import app
from .forms import contactForm
from flask.ext.mail import Message
from app import app, mail
from config import ADMINS

@app.route('/index')
@app.route('/index.html')
def index():
 return render_template("index.html")

@app.route('/about_us.html')
def about_us():
 return render_template("about_us.html")

@app.route('/contact.html',methods = ['GET', 'POST'])
def contact():
 form=contactForm()
 if form.validate_on_submit():
        msg = Message(u'致AIGame研究小组', sender = ADMINS[0], recipients = ADMINS)
        msg.body = form.suggest.data
        with app.app_context():
           mail.send(msg)
        return redirect('/index')
 return render_template("contact.html",form=form)
