
# Student Management System API

This is a backend API for a Student Management System built using **FastAPI** and **MongoDB**. It supports CRUD operations for managing student data and connects to a MongoDB Atlas cluster.

---

## Features
- **Create Students**: Add a new student to the database.
- **List Students**: Retrieve a list of students with optional filters (age, country).
- **Fetch Student by ID**: Get details of a specific student.
- **Update Student**: Modify details of an existing student.
- **Delete Student**: Remove a student from the database.

---

## Tech Stack
- **Language**: Python
- **Framework**: FastAPI
- **Database**: MongoDB Atlas (M0 Cluster)

---

## Requirements

### Dependencies
Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```
fastapi
uvicorn
pymongo
python-dotenv
```

---

## Environment Variables

The application requires a `.env` file or environment variables with the following details:

- **MONGO_URI**: MongoDB connection string (for MongoDB Atlas).

Example `.env` file:
```
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>?retryWrites=true&w=majority
DATABASE_NAME=name of database
```


## Running the Application

### Locally
Run the application locally using the following command:

```bash
uvicorn app.main:app --reload
```

## Testing the API

- **Base URL**: `http://127.0.0.1:8000/` (local) or Render's public URL.
- Use tools like Postman or `curl` to interact with the endpoints.

### Endpoints

#### Root
- **GET /**: Returns a welcome message.

#### Students
- **POST /students**: Add a new student.
- **GET /students**: List all students with optional filters (age, country).
- **GET /students/{id}**: Fetch a specific student by ID.
- **PATCH /students/{id}**: Update details of a student.
- **DELETE /students/{id}**: Delete a student by ID.

---
