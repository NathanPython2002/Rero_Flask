from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    """A simple route that returns Hello Rero+."""
    return render_template('index.html')

@app.route("/help")
def help_page():
    """A route that returns the help page."""
    return render_template('help.html')
