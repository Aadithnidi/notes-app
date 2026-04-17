# Notes App (Full-Stack)

A full-stack Notes Application built using FastAPI for the backend and HTML/JavaScript for the frontend. The application allows users to create, view, edit, and delete notes through a simple and interactive interface.

---

## 🚀 Live Demo

* Frontend: https://notes-app-psi-three.vercel.app
* Backend API: https://notes-app-u95u.onrender.com/docs

---

## 🛠️ Tech Stack

**Frontend**

* HTML
* JavaScript

**Backend**

* FastAPI (Python)

**Database**

* SQLite

**Deployment**

* Backend: Render
* Frontend: Vercel

---

## ✨ Features

* Create new notes
* View all notes
* Edit existing notes (inline editing)
* Delete notes
* REST API with full CRUD functionality
* Interactive frontend connected to live backend

---

## 📁 Project Structure

```
notes-app/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── notes.db
│
├── frontend/
│   └── index.html
│
├── .gitignore
├── vercel.json
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/Aadithnidi/notes-app.git
cd notes-app
```

---

### 2. Set up virtual environment

```
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install -r backend/requirements.txt
```

---

### 4. Run backend server

```
uvicorn backend.main:app --reload
```

---

### 5. Open frontend

Open `frontend/index.html` in your browser.

---

## 🧠 What I Learned

* Building REST APIs using FastAPI
* Handling CRUD operations and database interactions
* Connecting frontend to backend using fetch API
* Debugging real-world issues (CORS, deployment, API integration)
* Using Git and GitHub for version control
* Deploying full-stack applications using Render and Vercel
* Structuring projects with separate frontend and backend

---

## 📌 Future Improvements

* Add user authentication (login/signup)
* Improve UI/UX with modern styling (e.g., Tailwind CSS)
* Migrate to a production database (PostgreSQL)
* Add search and filtering functionality

---

## 👤 Author

Built by Aadith
