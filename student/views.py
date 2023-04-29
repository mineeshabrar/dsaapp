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
    event = collection_name.find({})
    
    for e in event:
        e = e["events"]

        for s in students:
                
                if s["sid"] == sid:
                    # for eventsOrg in s["events_organization"]:
                    #     eventsOrganized[e[eventsOrg]["date"]] = e[eventsOrg]["name"]

                    # for eventsPar in s["events_participation"]:
                    #     eventsParticipated[e[eventsPar]["date"]] = e[eventsPar]["name"]
                    
                    # print(eventsOrganized)
                    # print(eventsParticipated)
                    
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
