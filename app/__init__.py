from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

<<<<<<< HEAD
# setup database connection
=======
>>>>>>> 6271fe8217554b1d2f371e734a677a03334151e5
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
<<<<<<< HEAD

    # build all modules Flask application will need
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        from .import routes, models

        from app.blueprints.auth import bp as auth
        app.register_blueprint(auth)

=======

    # build all modules Flask application will need
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        from .import routes, models

        from app.blueprints.auth import bp as auth
        app.register_blueprint(auth)

>>>>>>> 6271fe8217554b1d2f371e734a677a03334151e5
    return app