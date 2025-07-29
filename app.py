from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    """A simple route that returns Hello Rero+."""
    return "Hello Rero+"
