from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Todo List API",
        "description": "A todo list API built with Flask and Swagger UI",
        "version": "1.0",
    },
    "basePath": "http://localhost:5000/"
})

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    complete = db.Column(db.Boolean, default=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Home endpoint that loads and displays all tasks or creates a new one.

    ---
    tags:
      - name: Todo List

    parameters:
      - name: taskContent
        in: formData
        type: string
        description: The content of the task.

    responses:
      200:
        description: Successfully retrieved or added tasks.
    """
    try:
        if request.method == 'POST':
            content = request.form['taskContent']
            new_task = TodoList(content=content)

            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/')

            except:
                return 'There was an issue adding your task'

        else:
            tasks = TodoList.query.order_by(TodoList.date_created).all()
            return render_template('index.html', tasks=tasks)

    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route('/delete/<int:id>')

def delete(id):
    """
        Endpoint to delete a task by ID.

        ---
        tags:
          - name: Todo List

        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: The ID of the task to be deleted.

        responses:
          200:
            description: Task deleted successfully.
          404:
            description: Task not found.
        """
    try:
        if id < 0:
            return redirect('/')
        db.session.delete(TodoList.query.get_or_404(id))
        db.session.commit()
        return redirect('/')

    except Exception as e:
            return f"An error occurred: {str(e)}"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    """
        Endpoint to update a task by ID.

        ---
        tags:
          - name: Todo List

        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: The ID of the task to be updated.
          - name: updateContent
            in: formData
            type: string
            description: The updated content of the task.

        responses:
          200:
            description: Task updated successfully.
          404:
            description: Task not found.
        """
    try:
        task = TodoList.query.get_or_404(id)

        if request.method == 'POST':
            task.content = request.form['updateContent']

            try:
                db.session.commit()
                return redirect('/')
            except:
                return 'There was an issue updating your task'

        else:
            return render_template('update.html', task=task)

    except Exception as e:
        return f"An error occurred: {str(e)}"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    tdList = TodoList()

    app.run(host="0.0.0.0", port=int("5000"), debug=True)
