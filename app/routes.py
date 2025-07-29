from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route("/")
def hello():
    """A simple route that returns Hello Rero+."""
    return render_template('index.html')

@bp.route("/help")
def help_page():
    """A route that returns the help page."""
    return render_template('help.html')
