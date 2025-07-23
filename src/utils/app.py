from flask import Flask
from .db import db
from ..routes.authRouter import auth_bp
from ..routes.rootRouter import root_bp

def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder='../views'
    )
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@localhost:3306/fairy?charset=utf8mb4',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)
    app.register_blueprint(root_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        from src.utils.model import User, create_test_user
        db.create_all()
        create_test_user()

    return app
