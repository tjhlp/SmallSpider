from flask import Blueprint

index_blu = Blueprint("index", __name__)

from modules.index.view import views