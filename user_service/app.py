from flask import Flask
from flask_restful import Api
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app