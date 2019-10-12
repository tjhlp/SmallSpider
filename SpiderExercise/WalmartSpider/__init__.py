from flask import Flask

def create_app():
    # register app
    app = Flask(__name__)
    return app
