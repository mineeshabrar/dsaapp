from django.shortcuts import render, redirect
from components.conf import *
from components.get_event_details import get_event_details
import pandas as pd
from datetime import date, datetime
from components.get_club_name import get_club_name
from django.core.files.storage import default_storage
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

def isHead(request):
    collection_name = db["secy_email"]

    head_emails = collection_name.find({})
    for head_email in head_emails:
        head_email = head_email["emails"]

        if request.user.email in head_email:
            return True

        return False

@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def event_details(request, event_id, club_name=""):
    if(request.session["role"]=='student'):
        return redirect('/')
    event = get_event_details(event_id)
    return render(request, "event_view.html", {"event": event, "isHead": isHead(request)})

@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def secy_add_event(request, club_name):
    if(request.session["role"]=='student'):
        return redirect('/')
    return render(request, "add_event.html", {"club_name": club_name,"role":'secy'})

@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def proficiency_list(request, club_name):
    if(request.session["role"]=='student'):
        return redirect('/')
    collection_name = db["students"]
    students = collection_name.find({})

    proficiency_list = []
    for student in students:
        if student["prof"] == club_name:
            proficiency_list.append(student)

    return render(request, "proficiency_list.html", {"students": proficiency_list,"club_name": club_name})

@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def secy_view(request, club_name):
    if(request.session["role"]=='student'):
        return redirect('/')
    collection_name = db["societies"]
    clubs = collection_name.find({})

    for club in clubs:
        if club["club_name"] == club_name:
            events = []
            for event in club["events"]:
                events.append(get_event_details(event))

            events = sorted(events, key=lambda x: datetime.strptime(x["date"], '%d-%m-%Y'), reverse=True)
            return render(request, "secy_landing_page.html", {"club_name": club_name, "events": events})

@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def secy_add_event_data(request):
    if(request.session["role"]=='student'):
        return redirect('/')
    if request.method == "POST":
        event_name = ((request.POST["EventName"]).title())
        event_description = ((request.POST["EventDescription"]).capitalize())
        sanction = request.POST["CollegeSanction"]
        sponsorship = request.POST["Sponsorship"]
        college_level = request.POST["College"]
        ParticipantCount = request.POST["ParticipantCount"]
        organisersFile = request.FILES["organisersFile"].read()
        participantsFile = request.FILES["participantsFile"].read()
        event_date_temp = request.POST["EventDate"]
        # convert date to dd-mm-yyyy
        event_date_temp = event_date_temp.split("-")
        event_date = event_date_temp[2] + "-" + event_date_temp[1] + "-" + event_date_temp[0]


        df = pd.read_excel(organisersFile, usecols=[0])
        organisersList = df["SID"].tolist()
        organisersList = [str(x) for x in organisersList]
        print("Organisers List: {}".format(organisersList))

        df = pd.read_excel(participantsFile, usecols=[0])
        participantsList = df["SID"].tolist()
        participantsList = [str(x) for x in participantsList]
        print("Participants List: {}".format(participantsList))

        club_name = get_club_name(request.user.email)
        event_id = ""

        collection_name = db["events"]
        events = collection_name.find({})

        collection_name = db["societies"]
        clubs = collection_name.find({})
        
        for club in clubs:
            if club["club_name"] == club_name:
                year = str(date.today().year)[-2:]

                if len(club["events"]) < 1:
                    event_id = club_name + year + "001"

                else:
                    event_id = club_name + year + str(len(club["events"]) + 1).zfill(3)

                if "poster" in request.FILES:
                    poster_file = request.FILES["poster"]
                    poster_name = event_id + '.' + poster_file.name.split('.')[-1]
                    poster_path = os.path.join(settings.MEDIA_ROOT, 'static', 'images', 'posters', poster_name)
                    with open(poster_path, 'wb+') as f:
                        for chunk in poster_file.chunks():
                            f.write(chunk)

                new_event = {
                    "name": event_name,
                    "club_name": club_name,
                    "description": event_description,
                    "event_organization": organisersList,
                    "event_participation": participantsList,
                    "participants_greater_than_250": ParticipantCount,
                    "event_id": event_id,
                    "sanction": sanction,
                    "sponsorship": sponsorship,
                    "college_level": college_level,
                    "date": event_date
                }

                club["events"].append(event_id)
                collection_name.update_one({"club_name": club_name}, {"$set": club})

                collection_name = db["events"]
                collection_name.insert_one(new_event)
        
                collection_name = db["students"]
                students = collection_name.find({})

                for student in students:
                    if student["sid"] in organisersList:
                        student["events_organization"].append(event_id)
                        print(student["events_organization"])
                        collection_name.update_one({"sid": student["sid"]}, {"$set": student})


                    if student["sid"] in participantsList:
                        student["events_participation"].append(event_id)
                        print(student["events_participation"])
                        collection_name.update_one({"sid": student["sid"]}, {"$set": student})

    return redirect("/secy/{}".format((club_name)))
