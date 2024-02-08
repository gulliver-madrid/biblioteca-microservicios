from .. import config  # pyright: ignore [reportUnusedImport]
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    environment_configuration = os.environ["CONFIGURATION_SETUP"]

    app.config.from_object(environment_configuration)

    db.init_app(app)

    with app.app_context():
        # Register blueprint
        return app
