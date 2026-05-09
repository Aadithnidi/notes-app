# Notes App (Full-Stack)

A full-stack Notes Application built using FastAPI for the backend and HTML/JavaScript for the frontend. The application allows users to create, view, edit, and delete notes through a simple and interactive interface. The project also includes foundational deployment and production practices such as dependency management, environment configuration, and containerization setup.

---

## Live Demo

- Frontend: https://notes-app-psi-three.vercel.app
- Backend API: https://notes-app-u95u.onrender.com/docs

---

## Tech Stack

**Frontend**
- HTML
- JavaScript

**Backend**
- FastAPI (Python)

**Database**
- SQLite

**Deployment / DevOps**
- Docker
- Render
- Vercel
- Git & GitHub

---

## Features

- Create new notes
- View all notes
- Edit existing notes inline
- Delete notes
- REST API with full CRUD functionality
- Interactive frontend connected to a live backend
- Separate backend and frontend structure
- Dependency management using `requirements.txt`
- Environment configuration using `.env`
- Docker-based backend setup using `Dockerfile`

---

## Project Structure

```plaintext
notes-app/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── .env
│   └── notes.db
│
├── frontend/
│   └── index.html
│
├── .gitignore
├── vercel.json
└── README.md
````

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Aadithnidi/notes-app.git
cd notes-app
```

### 2. Set up a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Run the backend server

```bash
uvicorn backend.main:app --reload
```

### 5. Open the frontend

Open `frontend/index.html` in your browser.

---

## What I Learned

* Building REST APIs using FastAPI
* Handling CRUD operations and database interactions
* Connecting frontend to backend using the Fetch API
* Debugging real-world issues such as CORS and API integration
* Using Git and GitHub for version control
* Deploying a full-stack application using Render and Vercel
* Structuring a project with separate frontend and backend folders
* Managing dependencies with `requirements.txt`
* Using environment variables for configuration
* Creating a Dockerfile for backend containerization

---

## Future Improvements

* Add user authentication
* Improve UI/UX with modern styling
* Migrate to PostgreSQL
* Add search and filtering functionality

---

## Author

Built by Aadith

```
