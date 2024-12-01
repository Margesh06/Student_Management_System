from fastapi import FastAPI
from app.routes.student_routes import router as student_router
from app.config import init_db

app = FastAPI()

# Initialize database
init_db()

# Include student routes
app.include_router(student_router, prefix="/students", tags=["Students"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Student Management System API"}
