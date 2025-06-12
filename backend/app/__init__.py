from flask import Flask
from flask_cors import CORS
from .extensions import db
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    # enable CORS for all routes by default for this API to be accessed by frontend ONLY with localhost
    CORS(app, origins=["http://localhost:5173"])
    register_routes(app)

    return app