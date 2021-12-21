from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route("/")
def index():
    return render_template("home.html", ux={'light_theme':True})

@app.route("/page1")
def page1():
    return render_template("page1.html", **{'greeting': 'Hello from Flask!'}, ux={'light_theme':True})

@app.route("/page2")
def page2():
    return render_template("page2.html", ux={'admin':True})

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form, ux={'admin':True})