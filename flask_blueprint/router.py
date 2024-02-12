from flask import jsonify
from dispatcher import dispatcher_bp

# Define your routes here and register them with the dispatcher blueprint
@dispatcher_bp.route('/')
def index():
    return jsonify({'message': 'Welcome to the dispatcher!'})

@dispatcher_bp.route('/hello')
def hello():
    return jsonify({'message': 'Hello from dispatcher!'})
