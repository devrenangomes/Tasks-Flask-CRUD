import pytest, requests

BASE_URL = 'http://127.0.0.1:5001'
tasks = []

# Create test

def test_create_task():
    new_task_data = {
        'title': 'Nome nova tarefa',
        'description': 'Descrição nova tarefa'
    }

    response = requests.post(f'{BASE_URL}/tasks', json = new_task_data)
    assert response.status_code == 200


