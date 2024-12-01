def serialize_student(student):
    student["id"] = str(student["_id"])
    del student["_id"]
    return student
