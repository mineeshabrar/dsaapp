from django.shortcuts import render
from pymongo import MongoClient
from majorProject.conf import connection_string

client = MongoClient(connection_string)
db = client['dsaapp-db']

def isHead(request):
    print("*********************")

    collection_name = db["head_email"]
    print("*********************")

    head_emails = collection_name.find({})
    for h in head_emails:
        h = h["emails"]

        if request.user.email in h:
            return True


def secy_view(request):
    collection_name = db["student_student"]

    students = collection_name.find({})
    for s in students:
        s = s['students']
        return render(request, 'secy_home_page.html', {"students" : s})
