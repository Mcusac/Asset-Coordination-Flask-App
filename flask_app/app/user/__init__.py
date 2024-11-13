# app/user/__init__.py

from flask import Blueprint

# Initialize the user blueprint
user_bp = Blueprint('user', __name__)

# Import routes so they’re registered with the blueprint
from . import routes
