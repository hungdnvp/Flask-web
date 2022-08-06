from flask_login import current_user, login_user, logout_user,login_required
from flask import flash, redirect, render_template,request, url_for
from . import app,db
from . import forms
from .models import Admin
from datetime import datetime

# luu thoi diem truy cap lan cuoi
@app.before_request
def before_request():
  if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

# Trang chinh
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Home')

# dang nhap
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

# Dang Xuat
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
# bai viet
@app.route('/post')
@login_required
def post():
    return render_template('index.html',title='Home',posts = current_user.posts)

# thong tin ca nhan
@app.route('/admin/<username>')
@login_required
def admin(username):
    admin = Admin.query.filter_by(username = username).first_or_404()
    posts = [
        {'author':admin , 'body': 'Bai viet #1'},
        {'author':admin , 'body': 'Bai viet #2'}
    ]
    return render_template('admin.html',admin = admin,posts=posts)

#chinh sua thong tin ca nhan
@app.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
    form = forms.EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.fullname = form.fullname.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        form.fullname.data = current_user.fullname
    return render_template('edit_profile.html', title='Edit Profile', form=form)

# dang ki user
@app.route('/register',methods=['GET','POST'])
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        fullname = form.fullname.data
        email = form.email.data
        password = form.password.data
        new_u = Admin(username=username,fullname=fullname,email=email)
        new_u.set_password(password)
        db.session.add(new_u)
        db.session.commit()
        flash('Register successfull')
        return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('register.html', title='Register', form=form)
    return render_template('register.html', title='Register', form=form)
    



