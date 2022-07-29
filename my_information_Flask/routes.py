from flask_login import current_user, login_user, logout_user,login_required
from flask import flash, redirect, render_template,request, url_for
from . import app
from . import forms
from .models import Admin

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Home')

@app.route('/login',methods =('GET','POST'))
def login():
    if current_user.is_authenticated:
       return redirect(url_for('index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin is None or not admin.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(admin, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
@app.route('/post')
@login_required
def post():
    return render_template('index.html',title='Home',posts = current_user.posts)



