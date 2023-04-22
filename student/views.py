from django.shortcuts import render
from pymongo import MongoClient


def student_view_data(request, name = None, sid = None, prof = None):
    connection_string = "mongodb://localhost:27017/?retryWrites=true&w=majority"
    client = MongoClient(connection_string)
        
    db = client['dsaapp-db']
    collection_name = db["student_student"]

    students = collection_name.find({})

    for s in students:
        s = s['students']

        for element in s:
            if(element['sid'] == sid):
                return render(request, 'nav_bar_student.html', element)

