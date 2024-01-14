import pytest
from main import app, db, TodoList

# Fixture to create a test client for the Flask app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_index(client):
    response = client.get('/')

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check for specific HTML elements or attributes
    assert b'<title>Todo List</title>' in response.data
    assert b'<h1>Todo List</h1>' in response.data
    assert b'<input type="text" name="taskContent" placeholder="Enter Task">' in response.data
    assert b'<input type="submit" value="Add Task">' in response.data

# Test adding a task
def test_add_task(client):
    response = client.post('/', data={'taskContent': 'Test Task'}, follow_redirects=True)
    assert b'Test Task' in response.data

# Test updating a task
def test_update_task(client):
    task = TodoList(content='Test Task')
    db.session.add(task)
    db.session.commit()

    response = client.post(f'/update/{task.id}', data={'updateContent': 'Updated Task'}, follow_redirects=True)
    assert b'Updated Task' in response.data

# Test deleting a task
def test_delete_task(client):
    task = TodoList(content='Test Task')
    db.session.add(task)
    db.session.commit()

    response = client.get(f'/delete/{task.id}', follow_redirects=True)
    assert b'Test Task' not in response.data

# Cleanup the database after all tests are done
def teardown_module():
    with app.app_context():
        db.drop_all()