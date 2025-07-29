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

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error handler."""
    return render_template('404.html'), 404
