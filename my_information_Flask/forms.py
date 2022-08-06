from flask_wtf import FlaskForm
from wtforms import ( StringField, PasswordField,
 BooleanField, SubmitField,TextAreaField )
from wtforms.validators import DataRequired,ValidationError,Length
 
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    fullname = StringField('Fullname', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    fullname = StringField('Fullname', validators=[DataRequired()])
    email = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')