from django.shortcuts import render
from pymongo import MongoClient

# Create your views here.

def secy_view(request):
    connection_string = "mongodb://localhost:27017/?retryWrites=true&w=majority"
    client = MongoClient(connection_string)
        
    db = client['dsaapp-db']
    collection_name = db["student_student"]

    students = collection_name.find({})
    for s in students:
        s = s['students']
        return render(request, 'secy_home_page.html', {"students" : s})
