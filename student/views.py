from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from datetime import datetime
from components.get_event_details import get_event_details
from components.conf import db


def student_final_view_data(request, sid):
    eventsOrganized = []
    eventsParticipated = []

    collection_name = db["students"]
    students = collection_name.find({})

    collection_name = db["events"]

    for student in students:    
        if student["sid"] == sid:
            if len(student["events_organization"]) != 1:
                events_organized = []
                for event in student["events_organization"]:
                    events_organized.append(get_event_details(event))
                
                eventsOrganized = sorted(events_organized, key=lambda x: x["date"], reverse=True)

            if len(student["events_participation"]) != 1:
                events_participated = []
                for event in student["events_participation"]:
                    events_participated.append(get_event_details(event))

                eventsParticipated = sorted(events_participated, key=lambda x: x["date"], reverse=True)
                
            return render(request, "student_landing_page.html", {"student": student, "eventsOrganized": eventsOrganized, "eventsParticipated": eventsParticipated})


def student_view_data(request):
    collection_name = db["students"]
    students = collection_name.find({})

    for student in students:
        if student["email"] == request.user.email:
            sid = student["sid"]
            return redirect(f"{sid}/")

    messages.error(request, "{} is not authenticated. Please contact DSA office.".format(request.user.email))
    logout(request)
    return HttpResponseRedirect("/")
