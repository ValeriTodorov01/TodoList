# Flask Todo List API

## Overview

This is a simple Todo List API built with Flask, SQLAlchemy, and Swagger UI for documentation. It allows you to manage tasks by providing endpoints for creating, updating, and deleting tasks.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.12
- Flask
- Flask-SQLAlchemy
- flasgger

Install the required dependencies using:

```bash
pip install Flask Flask-SQLAlchemy flasgger
```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ValeriTodorov01/TodoList.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repository
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```

Replace `your-username` and `your-repository` with your GitHub username and repository name, respectively. Also, replace `your_app_name.py` with the actual name of your Flask application script.

## API Endpoints

### Home Endpoint

- **URL:** `/`
- **Method:** `GET` or `POST`
- **Description:** Home endpoint that loads and displays all tasks or creates a new one.

  #### Parameters:

  - `taskContent` (in formData, type: string): The content of the task.

  #### Responses:

  - `200 OK`: Successfully retrieved or added tasks.
  
### Delete Endpoint

- **URL:** `/delete/<int:id>`
- **Method:** `GET`
- **Description:** Endpoint to delete a task by ID.

  #### Parameters:

  - `id` (in path, type: integer, required: true): The ID of the task to be deleted.

  #### Responses:

  - `200 OK`: Task deleted successfully.
  - `404 Not Found`: Task not found.

### Update Endpoint

- **URL:** `/update/<int:id>`
- **Method:** `GET` or `POST`
- **Description:** Endpoint to update a task by ID.

  #### Parameters:

  - `id` (in path, type: integer, required: true): The ID of the task to be updated.
  - `updateContent` (in formData, type: string): The updated content of the task.

  #### Responses:

  - `200 OK`: Task updated successfully.
  - `404 Not Found`: Task not found.

## Swagger Documentation

The API is documented using Swagger UI, which can be accessed at [http://localhost:5000/apidocs/index.html](http://localhost:5000/apidocs/index.html) when the application is running.
