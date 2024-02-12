from flask import Blueprint

# Create a Blueprint instance for the dispatcher
dispatcher_bp = Blueprint('dispatcher', __name__)

# Import the routes from other files and register them with the dispatcher Blueprint
from dispatcher import routes
