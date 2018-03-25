#coding:utf8

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField('提交')