from flask_smorest import Blueprint

bp = Blueprint('answers', __name__, url_prefix='/answer')

from . import routes