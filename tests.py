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

def test_get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    assert response.status_code == 200

    response_json = response.json()
    assert 'tasks' in response_json
    assert 'total_tasks' in response_json


def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200
        response_json = response.get_json()
        assert task_id == response_json['id']

