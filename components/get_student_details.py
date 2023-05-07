from .conf import *

def get_student_details(sid):
    collection_name = db["students"]
    students = collection_name.find({})

    for student in students:
        if student["sid"] == sid:
            return student