from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from components.conf import db


def student_final_view_data(request, sid):
    eventsOrganized = {}
    eventsParticipated = {}

    collection_name = db["students"]
    students = collection_name.find({})

    collection_name = db["events"]

    for s in students:
                
        if s["sid"] == sid:

            if len(s["events_organization"]) != 1:
                for eventsOrg in s["events_organization"]:
                    event = collection_name.find_one({"event_id": eventsOrg})
                    eventsOrganized[event["date"]] = event["name"]
                    
            if len(s["events_participation"]) != 1:
                for eventsPar in s["events_participation"]:
                    event = collection_name.find_one({"event_id": eventsPar})
                    eventsParticipated[event["date"]] = event["name"]
                    
            return render(request, "student_landing_page.html", {"student": s, "eventsOrganized": eventsOrganized, "eventsParticipated": eventsParticipated})


def student_view_data(request):
    collection_name = db["students"]

    students = collection_name.find({})

    for s in students:
           if s["email"] == request.user.email:
                sid = s["sid"]
                return redirect(f"{sid}/")

    messages.error(request, "{} is not authenticated. Please contact DSA office.".format(request.user.email))
    logout(request)
    return HttpResponseRedirect("/")
