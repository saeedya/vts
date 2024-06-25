from flask import Blueprint

user_bp = Blueprint('user_bp', __name__)

from .routes import UserResource, UserListResource
from app import api

api.add_resource(UserListResource, '/')
api.add_resource(UserResource, '/<int:user_id>')