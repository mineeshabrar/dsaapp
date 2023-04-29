from django.shortcuts import render, redirect
from components.conf import *
from components.get_event_details import get_event_details
from bson import ObjectId
import pandas as pd
import datetime


def isHead(request):
    collection_name = db["secy_email"]

    head_emails = collection_name.find({})
    for h in head_emails:
        h = h["emails"]

        if request.user.email in h:
            return True

        else:
            return False


def event_details(request, club_name, event_id):
    event = get_event_details(event_id)
    return render(request, "event_view.html", {"event": event})


def secy_add_event(request):
    return render(request, "add_event.html")


def proficiency_list(request):
    club_name = request.user.email.split('@')[0]

    collection_name = db["students"]
    students = collection_name.find({})

    proficiency_list = []
    for student in students:
        if student["prof"] == club_name:
            proficiency_list.append(student)

    return render(request, "proficiency_list.html", {"students": proficiency_list})


def secy_view(request, club_name):
    collection_name = db["societies"]
    clubs = collection_name.find({})

    for club in clubs:
        if club["club_name"] == club_name:
            events = []
            for event in club["events"]:
                events.append(get_event_details(event))
            return render(request, "secy_landing_page.html", {"club_name": club_name, "events": events})


def secy_add_event_data(request):
    if request.method == "POST":
        event_name = ((request.POST["EventName"]).title())
        event_description = ((request.POST["EventDescription"]).capitalize())
        sanction = request.POST["CollegeSanction"]
        sponsorship = request.POST["Sponsorship"]
        college_level = request.POST["College"]
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

        club_name = request.user.email.split('@')[0]
        event_id = ""

        collection_name = db["events"]
        events = collection_name.find({})

        collection_name = db["societies"]
        clubs = collection_name.find({})
        
        for club in clubs:
            if club["club_name"] == club_name:
                year = str(datetime.date.today().year)[-2:]

                if len(club["events"]) < 1:
                    event_id = club_name + year + "001"

                else:
                    event_id = club_name + year + str(len(club["events"]) + 1)

                new_event = {
                    "name": event_name,
                    "club_name": club_name,
                    "description": event_description,
                    "event_organization": organisersList,
                    "event_participation": participantsList,
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
