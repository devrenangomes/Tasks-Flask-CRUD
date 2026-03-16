# Tasks Flask CRUD API

A simple RESTful API for managing tasks, built with Python and Flask. This project implements basic CRUD (Create, Read, Update, Delete) operations.

## Features

- **Create** new tasks with a title and description.
- **Read** a list of all tasks or retrieve a specific task by its ID.
- **Update** existing tasks (title, description, and completion status).
- **Delete** a task by its ID.
- Automated API testing using `pytest` and `requests`.

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- Virtual environment (recommended)

## Installation & Setup

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd Tasks-Flask-CRUD
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # .venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the Flask development server:

```bash
python app.py
```

The server will start running at `http://127.0.0.1:5001`.

## API Endpoints

| Method | Endpoint | Description | Request Body (JSON) |
| :--- | :--- | :--- | :--- |
| `POST` | `/tasks` | Create a new task | `{"title": "string", "description": "string"}` |
| `GET` | `/tasks` | List all tasks | None |
| `GET` | `/tasks/<id>` | Get a specific task | None |
| `PUT` | `/tasks/<id>` | Update a specific task | `{"title": "string", "description": "string", "completed": boolean}` |
| `DELETE` | `/tasks/<id>` | Delete a specific task | None |

### Task Model
```json
{
  "id": 1,
  "title": "Task title",
  "description": "Task description",
  "completed": false
}
```

## Testing

This project includes automated tests using `pytest` and `requests`. The test suite verifies the functionality of all CRUD endpoints.

To run the tests, ensure your virtual environment is activated and the Flask server is running in another terminal window, then execute:

```bash
pytest tests.py -v
```
