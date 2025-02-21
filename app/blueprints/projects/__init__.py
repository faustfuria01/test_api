from flask import Blueprint

bp_project = Blueprint('projects', __name__, url_prefix='/projects')

from app.blueprints.projects import routes