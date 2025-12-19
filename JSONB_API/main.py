from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, File
from schemas import FileCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Create file metadata
@app.post("/files")
def create_file(file: FileCreate, db: Session = Depends(get_db)):
    new_file = File(file_metadata=file.file_metadata)
    db.add(new_file)
    db.commit()
    db.refresh(new_file)
    return {
        "id": new_file.id,
        "file_metadata": new_file.file_metadata
    }
