from flask_smorest import Blueprint

bp = Blueprint('doctors', __name__, description='Ops on Doctors')

from . import routes