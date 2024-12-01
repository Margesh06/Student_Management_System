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

# Ensure the app binds to the correct port
if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT is not set
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)