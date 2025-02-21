from flask import Response
from app.blueprints.projects import bp_project
from app.blueprints.projects.service import ProjectService
from app.helpers.response_helper import success, error


@bp_project.route('/', methods=['GET'])
def get_projects():
    """
    Get a list of all projects
    ---
    responses:
      200:
        description: List of projects
    """
    projects = ProjectService.get_all_projects()

    return success(
        message="Projects retrieved successfully",
        data=projects
    )

@bp_project.route('/<int:project_id>', methods=['GET'])
def get_project(project_id: int) -> tuple[Response, int]:
    """
    Get project by ID
    ---
    parameters:
      - name: project_id
        in: path
        type: integer
        required: true
        description: project ID
    responses:
      200:
        description: Project data
      404:
        description: Project not found
    """
    project = ProjectService.get_project_by_id(project_id)
    if project is None:
        return error(
            message={'error': 'Project not found'},
            http_status_code=404
        )

    return success(
        message="Project retrieved successfully",
        data=project
    )
