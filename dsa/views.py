from django.shortcuts import render, redirect
from components.conf import db


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
    return render(request, "add_event.html")


def dsa_view(request):
    collection_name = db["students"]
    student = collection_name.find({})
    students = []

    for s in student:
        students.append(s)
    
    print(students)
    return render(request, "dsa_landing_page.html", {"students": students})