from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from datetime import datetime
from components.get_event_details import get_event_details
from components.conf import db
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def student_final_view_data(request, sid, role = "student"):
    eventsOrganized = []
    eventsParticipated = []

    collection_name = db["students"]
    students = collection_name.find({})

    collection_name = db["events"]

    for student in students:    
        if student["sid"] == sid:
            eventsOrganized = []
            eventsParticipated = []
            if len(student["events_organization"]) > 0:
                for event in student["events_organization"]:
                    eventsOrganized.append(get_event_details(event))
                
                eventsOrganized = sorted(eventsOrganized, key=lambda x: datetime.strptime(x["date"], '%d-%m-%Y'))

            if len(student["events_participation"]) > 0:
                for event in student["events_participation"]:
                    eventsParticipated.append(get_event_details(event))

                eventsParticipated = sorted(eventsParticipated, key=lambda x: datetime.strptime(x["date"], '%d-%m-%Y'))
            return render(request, "student_landing_page.html", {"student": student, "eventsOrganized": eventsOrganized, "eventsParticipated": eventsParticipated, "role": role})

@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
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
@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def student_organized_events(request, sid,role = "student"):
    eventsOrganized = []
    eventsParticipated = []

    collection_name = db["students"]
    students = collection_name.find({})

    collection_name = db["events"]

    for student in students:    
        if student["sid"] == sid:
            eventsOrganized = []
            eventsParticipated = []
            if len(student["events_organization"]) > 0:
                for event in student["events_organization"]:
                    eventsOrganized.append(get_event_details(event))
                
                eventsOrganized = sorted(eventsOrganized, key=lambda x: datetime.strptime(x["date"], '%d-%m-%Y'))

            if len(student["events_participation"]) > 0:
                for event in student["events_participation"]:
                    eventsParticipated.append(get_event_details(event))

                eventsParticipated = sorted(eventsParticipated, key=lambda x: datetime.strptime(x["date"], '%d-%m-%Y'))
                
            return render(request, "student_organized_events.html", {"student": student, "eventsOrganized": eventsOrganized, "eventsParticipated": eventsParticipated, "role": role})

@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def student_participated_events(request, sid, role = "student"):
    eventsParticipated = []

    collection_name = db["students"]
    students = collection_name.find({})

    collection_name = db["events"]

    for student in students:    
        if student["sid"] == sid:
            eventsParticipated = []
            if len(student["events_participation"]) > 0:
                for event in student["events_participation"]:
                    eventsParticipated.append(get_event_details(event))

                eventsParticipated = sorted(eventsParticipated, key=lambda x: datetime.strptime(x["date"], '%d-%m-%Y'))
                
            return render(request, "student_participated_events.html", {"student": student,"eventsParticipated": eventsParticipated, "role": role})
