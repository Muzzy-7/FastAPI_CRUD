from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

notes =[]

class CreateNote(BaseModel):
    title: str
    note: str

class ResponseNote(BaseModel):
    id: int
    title: str
    note: str

@app.post("/notes", response_model=ResponseNote)
def create_note(note: CreateNote):
    if not notes:
        new_id = 1
    else:
        new_id = notes[-1]["id"] + 1

    new_note ={
        "id": new_id,
        "title": note.title,
        "note": note.note 
    }
    notes.append(new_note)    
    return new_note


@app.get("/notes/{notes_id}")
def get_note(notes_id: int):
    for note in notes:
        if note["id"] == notes_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

@app.put("/notes/{notes_id}", response_model=ResponseNote)
def update_note(notes_id:int, noteupdate: CreateNote):
    for note in notes:
        if note["id"] == notes_id:
            note["title"] = noteupdate.title
            note["note"] = noteupdate.note
            return note
    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/notes/{notes_id")
def deletenote(notes_id:int):
    for note in notes:
        if note["id"] == notes_id:
            notes.remove(note)
        return ("Note deleted")
    raise HTTPException(status_code=404, detail="Note not found")

@app.get("/notes")
def allnotes():
        return notes
    