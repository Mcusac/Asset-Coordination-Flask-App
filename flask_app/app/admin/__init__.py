# app/admin/__init__.py

from flask import Blueprint

# Initialize the admin blueprint
admin_bp = Blueprint('admin', __name__)

# Import routes so they’re registered with the blueprint
from . import routes
