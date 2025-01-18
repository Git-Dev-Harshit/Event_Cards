from flask import Flask
from app.routes.main_routes import bp
from app.utils.logger import logger

def create_app():

    app = Flask(__name__)
    logger.info("App Initialized")

    app.register_blueprint(bp)
    logger.info("Blueprints Registered")

    return app