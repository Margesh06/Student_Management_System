from fastapi import APIRouter, HTTPException, Query, Path
from app.models import Student, UpdateStudent
from app.config import db
from bson import ObjectId
from app.utils import serialize_student

router = APIRouter()

students_collection = db["students"]

@router.post("/", status_code=201)
async def create_student(student: Student):
    student_data = student.dict()
    result = students_collection.insert_one(student_data)
    return {"id": str(result.inserted_id)}

@router.get("/")
async def list_students(country: str = Query(None), age: int = Query(None)):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}

    students = students_collection.find(query)
    return {"data": [serialize_student(s) for s in students]}

@router.get("/{id}")
async def fetch_student(id: str = Path(...)):
    student = students_collection.find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return serialize_student(student)

@router.patch("/{id}", status_code=204)
async def update_student(id: str, student: UpdateStudent):
    update_data = {k: v for k, v in student.dict().items() if v is not None}
    if "address" in update_data:
        update_data["address"] = {k: v for k, v in update_data["address"].items() if v is not None}
    result = students_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return

@router.delete("/{id}")
async def delete_student(id: str):
    result = students_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
