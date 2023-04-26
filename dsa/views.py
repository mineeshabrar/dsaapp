from django.shortcuts import render, redirect
from pymongo import MongoClient
from majorProject.conf import connection_string

client = MongoClient(connection_string)
db = client['dsaapp-db']

def isDSA(request):
    collection_name = db["dsa_email"]

    dsa_emails = collection_name.find({})
    for h in dsa_emails:
        h = h["emails"]

        if request.user.email in h:
            return True
        
        else:
            return False


def dsa_add_event(request):
    return render(request, 'add_event.html')


def dsa_view(request):
    collection_name = db["student_student"]

    students = collection_name.find({})
    for s in students:
        s = s['students']
        return render(request, 'dsa_landing_page.html', {"students" : s})
