from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextInput

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], widget=TextInput("<v-text-field label='Regular'></v-text-field>"))
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')