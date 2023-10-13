from flask_smorest import Blueprint

bp = Blueprint('questions', __name__, url_prefix='/question')

from . import routes