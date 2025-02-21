import json
from datetime import datetime
from pathlib import Path
from flask import current_app
from app.models.project import Project
from app.schemas.project import ProjectSchema


class ProjectService:
    @staticmethod
    def load_projects():
        # Get the path to the data file
        data_file_path = Path(current_app.config['DATA_FILE'])

        # Return an empty list if the file does not exist
        if not data_file_path.exists():
            return []

        try:
            # Open and load the JSON data from the file
            with data_file_path.open('r', encoding='utf-8') as f:
                projects_data = json.load(f)
                # Create Project instances from the loaded data
                return [ProjectService._create_project(data) for data in projects_data]
        except json.JSONDecodeError:
            # Return an empty list if JSON decoding fails
            return []
        except Exception:
            # Return an empty list for any other exceptions
            return []

    @staticmethod
    def _create_project(data):
        try:
            # Parse start_date and end_date if available
            data['start_date'] = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
            end_date_str = data.get('end_date')
            data['end_date'] = datetime.strptime(end_date_str, '%Y-%m-%d').date() if end_date_str else None
            # Create and return a Project instance
            return Project(**data)
        except (KeyError, ValueError):
            # Return None if there is a KeyError or ValueError
            return None

    @staticmethod
    def get_all_projects():
        # Load all projects and serialize them using the schema
        projects = ProjectService.load_projects()
        schema = ProjectSchema(many=True)
        return schema.dump([p for p in projects if p is not None])

    @staticmethod
    def get_project_by_id(project_id: int):
        # Find a project by its ID
        projects = ProjectService.load_projects()
        project = next((p for p in projects if p and p.id == project_id), None)
        if project is None:
            return None
        # Serialize the found project using the schema
        schema = ProjectSchema()
        return schema.dump(project)