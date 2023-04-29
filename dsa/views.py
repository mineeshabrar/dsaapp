from django.shortcuts import render, redirect
from components.conf import db


def isDSA(request):
    collection_name = db["dsa_email"]

    dsa_emails = collection_name.find({})
    for dsa_email in dsa_emails:
        dsa_email = dsa_email["emails"]

        if request.user.email in dsa_email:
            return True

        else:
            return False


def dsa_add_event(request):
    return render(request, "add_event.html")


def dsa_view(request):
    collection_name = db["students"]

    students = collection_name.find({})
    for s in students:
        s = s["students"]
        return render(request, "dsa_landing_page.html", {"students": s})
