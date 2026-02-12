from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models, schemas, database

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/consultations/", response_model=schemas.ConsultationRequest)
def create_consultation(request: schemas.ConsultationRequestCreate, db: Session = Depends(get_db)):
    db_request = models.ConsultationRequest(
        name=request.name, 
        phone=request.phone,
        email=request.email,
        faculty=request.faculty,
        message=request.message
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

@app.get("/")
def read_root():
    return {"message": "API is running"}
