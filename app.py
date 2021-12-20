from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html", ux={'light_theme':True})

@app.route("/page1")
def page1():
    return render_template("page1.html", **{'greeting': 'Hello from Flask!'}, ux={'light_theme':True})

@app.route("/page2")
def page2():
    return render_template("page2.html", ux={'admin':True})