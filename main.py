from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = Path("notes.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
        """)


init_db()


class NoteIn(BaseModel):
    title: str
    content: str


class NoteOut(NoteIn):
    id: int


@app.get("/")
def root():
    return {"message": "Notes app is running"}


@app.get("/notes")
def list_notes():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, title, content FROM notes ORDER BY id DESC"
        ).fetchall()
    return [dict(row) for row in rows]


@app.post("/notes", response_model=NoteOut, status_code=201)
def create_note(note: NoteIn):
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO notes (title, content) VALUES (?, ?)",
            (note.title, note.content)
        )
        note_id = cursor.lastrowid
        row = conn.execute(
            "SELECT id, title, content FROM notes WHERE id = ?",
            (note_id,)
        ).fetchone()
    return dict(row)


@app.put("/notes/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note: NoteIn):
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE notes SET title = ?, content = ? WHERE id = ?",
            (note.title, note.content, note_id)
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Note not found")

        row = conn.execute(
            "SELECT id, title, content FROM notes WHERE id = ?",
            (note_id,)
        ).fetchone()
    return dict(row)


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Deleted"}