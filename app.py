from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    """A simple route that returns Hello Rero+."""
    return render_template('index.html')
