from app import app
from flask import render_template, flash, redirect, request,url_for
# from .forms import LoginForm
from . import forms


@app.route('/')
def hello():
    return render_template('index.html')

#url_for的使用
@app.route('test')
def test():
    return redirect(url_for('hello'))


@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_log = forms.LoginForm()
    if request.method == 'POST':
        openid = request.form.get('openid')
        print(openid + 'ab')
        if form_log.validate_on_submit():
            # flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
            return redirect('/index')
        elif not all([openid]):
            print(11)
            flash('openid或remeber_me为空')

    return render_template('login.html', form=form_log)


@app.route('/openid', methods=['GET', 'POST'])
def openid():
    form_log = forms.LoginForm()
    if request.method == 'POST':
        openid = request.form.get('openid')
        print(openid + 'ab')
        if form_log.validate_on_submit():
            return redirect('/index')

    return render_template('login_openid.html',
                           form=form_log,
                           providers=app.config['OPENID_PROVIDERS'])
