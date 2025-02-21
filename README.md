# Portfolio Projects API

REST API for managing portfolio projects on Flask.

### Install and run

### Using Docker

1. Clone the repository:
git clone <url repository>
cd portfolio-projects-api

2. Build and run the containers:
docker-compose up --build

3. Stop containers:
docker-compose down -v

### Without Docker

1. Create a virtual environment:
python -m venv venv
source venv/bin/activate # for Linux/Mac
venv\Scripts\activate # for Windows

2. Install dependencies:
pip install -r requirements.txt

3. Run the application:
flask run

## API Endpoints

### Get all projects
GET /api/projects

### Get project by ID
GET /api/projects/<id>

## Project data structure

{
  “id": 1,
  “name": ‘Project name’,
  “description": “job description”,
  { “technologies”: [“Python”, “Flask”, “Docker” ],
  “start_date": ‘2023-01-01’,
  “end_date": ”2023-06-30”
}

## Development

The project uses:
- Flask for the API
- Blueprint for code organization
- JSON files for data storage
- Docker for containerization

## Testing

Once launched, the API will be available at:
- http://localhost:5000/projects
- http://localhost:5000/projects/1