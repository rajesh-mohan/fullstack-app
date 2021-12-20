from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("cdn-vuetify-vue.html", **{'greeting': 'Hello from Flask!'})