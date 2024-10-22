from flask import Flask
from .routes.routes import planet_bp
#if using planets_path file for planets_bp it would look like the following
#from .routes.planets_path import planet_bp
def create_app(test_config=None):
    app = Flask(__name__)
    app.register_blueprint(planet_bp)
    return app
