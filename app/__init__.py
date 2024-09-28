from flask import Flask
from app.extensions import db, cache
from app.blueprints.tasks import tasks_bp
from app.blueprints.calendar import calendar_bp
from app.blueprints.grocery import grocery_bp
from app.blueprints.profile import profile_bp
from flask_migrate import Migrate
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)
    cache.init_app(app)

    # Register blueprints
    app.register_blueprint(tasks_bp)
    app.register_blueprint(calendar_bp)
    app.register_blueprint(grocery_bp)
    app.register_blueprint(profile_bp)

    migrate = Migrate(app, db)  # Initialize Flask-Migrate
    return app
