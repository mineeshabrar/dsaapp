from django.shortcuts import render, redirect
from pymongo import MongoClient
from django.contrib import messages
from allauth.exceptions import ImmediateHttpResponse
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from majorProject.conf import connection_string


def student_final_view_data(request, sid):
    eventsOrganized = {}
    eventsParticipated = {}
    client = MongoClient(connection_string)

    db = client["dsaapp-db"]
    collection_name = db["student_student"]

    students = collection_name.find({})

    collection_name = db["student_events"]
    event = collection_name.find({})
    
    for e in event:
        e = e["events"]

        for s in students:
            s = s["students"]

            for student in s:
                if student["sid"] == sid:

                    for eventsOrg in student["event_organization"]:
                        eventsOrganized[e[eventsOrg]["date"]] = e[eventsOrg]["name"]

                    for eventsPar in student["event_participation"]:
                        eventsParticipated[e[eventsPar]["date"]] = e[eventsPar]["name"]
                    
                    return render(request, "student_landing_page.html", {"student": student, "eventsOrganized": eventsOrganized, "eventsParticipated" : eventsParticipated})


def student_view_data(request):
    client = MongoClient(connection_string)

    db = client["dsaapp-db"]
    collection_name = db["student_student"]

    students = collection_name.find({})

    for s in students:
        s = s["students"]

        for student in s:
            if student["email"] == request.user.email:
                sid = student["sid"]
                return redirect(f"{sid}/")

        messages.error(request, "{} is not authenticated. Please contact DSA office.".format(request.user.email))
        logout(request)
        return HttpResponseRedirect("/")
