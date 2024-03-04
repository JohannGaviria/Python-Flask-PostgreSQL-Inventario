from flask import Blueprint, jsonify


main = Blueprint('index', __name__)


@main.route("/")
def index():
    return "Hello, World!"