#!/usr/bin/env python3
"""
Route module for the API
"""


from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.auth import Auth

# Import SessionAuth
from api.v1.auth.session_auth import SessionAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
AUTH_TYPE = os.getenv("AUTH_TYPE")


if AUTH_TYPE == "basic_auth":
    auth = BasicAuth()
elif AUTH_TYPE == "session_auth":
    auth = SessionAuth()

# Enable pretty print for JSON responses
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.before_request
def before_request() -> str:
    """
    Method to handle filtering of each request.
    """

    if auth is None:
        return

    # Define paths that don't require authentication
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']

    if not auth.require_auth(request.path, excluded_paths):
        return

    # Check for Authorization header
    if auth.authorization_header(request) is None:
        abort(401)

    # Check for current user
    """ Update the auth.current_user(request) to
    request.current_user."""
    request.current_user = auth.current_user(request)
    if request.current_user is None:
        abort(403)


@app.route('/api/v1/status', methods=['GET'])
def status() -> str:
    """
    Endpoint to return the status of the API.
    """
    return jsonify({"status": "OK"})


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """ Handle 401 Unauthorized error with a JSON response.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """ Handle 403 not allowing access to resource.
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
