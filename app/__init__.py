from flask import Flask, render_template
from app.routes import bp

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(bp)

    @app.errorhandler(404)
    def page_not_found(e):
        """Custom 404 error handler."""
        return render_template('404.html'), 404

    return app
