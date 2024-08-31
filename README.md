
# FastAPI To-Do List Application

This is a simple To-Do list application built using FastAPI, which demonstrates basic CRUD operations (Create, Read, Update, Delete).

## Project Structure

```
fastapi-todo/
│
├── main.py               # Main application file containing FastAPI routes
├── requirements.txt      # Dependencies required for the project
└── README.md             # Project documentation (this file)
```

## Requirements

To run this project, you need to have the following installed:

- **Python 3.8+**
- **Virtual Environment (optional but recommended)**
- **Uvicorn** (an ASGI server for running FastAPI applications)

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-todo.git
cd fastapi-todo
```

### 2. Create a Virtual Environment (Optional)

It’s recommended to create a virtual environment to manage dependencies:

```bash
python -m venv fastapi-env
```

### 3. Activate the Virtual Environment

- On **Windows**:

  ```bash
  .\fastapi-env\Scripts\Activate.ps1
  ```

- On **macOS/Linux**:

  ```bash
  source fastapi-env/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
uvicorn main:app --reload
```

### 6. Access the API

- Open your web browser and navigate to: `http://127.0.0.1:8000/`
- Explore the interactive API documentation:
  - **Swagger UI**: `http://127.0.0.1:8000/docs`
  - **ReDoc**: `http://127.0.0.1:8000/redoc`

## Endpoints

- **GET `/`**: Welcome message.
- **GET `/items/`**: Retrieve all items.
- **GET `/items/{item_id}`**: Retrieve a specific item by ID.
- **POST `/items/`**: Add a new item.
- **PUT `/items/{item_id}`**: Update an existing item.
- **DELETE `/items/{item_id}`**: Delete an item by ID.

## Requirements File

To create or update the `requirements.txt` file, you can use:

```bash
pip freeze > requirements.txt
```

This command will capture all the dependencies required for the project.

This project is open-source and available under the [MIT License](LICENSE).

```

