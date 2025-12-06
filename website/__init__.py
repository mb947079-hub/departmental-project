from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///college.db'
    db.init_app(app)

    # IMPORTANT: import ALL models
    from .models import User, Faculty, Student, Section

    # Create database & tables
    create_database(app)

    return app


def create_database(app):
    with app.app_context():
       db.create_all()