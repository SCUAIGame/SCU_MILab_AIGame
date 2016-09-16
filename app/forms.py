#coding=utf-8
from flask.ext.wtf import Form
from wtforms import validators,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class contactForm(Form):
    suggest = TextAreaField(u'致AIGames研究小组',validators=[DataRequired()],id='message')
    submit = SubmitField(u"发送",id='submit')

