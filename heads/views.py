from django.shortcuts import render, redirect
from majorProject.conf import *
from bson import ObjectId
import pandas as pd

# club_name = request.user.email.split('@')[0]
club_name = "aabhaschopra.bt19ele"


def isHead(request):
    collection_name = db["secy_email"]

    head_emails = collection_name.find({})
    for h in head_emails:
        h = h["emails"]

        if request.user.email in h:
            return True

        else:
            return False


def event_details(request, event_id):
    collection_name = db["societies"]

    clubs = collection_name.find({})
    for c in clubs:
        c = c["clubs"]

    events = c["aabhaschopra.bt19ele"]
    for event in events:
        if event["event_id"] == event_id:
            return render(request, "event_view.html", {"event": event})


def secy_add_event(request):
    return render(request, "add_event.html")


def proficiency_list(request):
    collection_name = db["students"]
    students = collection_name.find({})

    for s in students:
        s = s["students"]

        proficiency_list = []
        for student in s:
            if student["prof"] == club_name:
                proficiency_list.append(student)

        return render(request, "proficiency_list.html", {"students": proficiency_list})


def secy_view(request):
    collection_name = db["societies"]

    clubs = collection_name.find({})
    for c in clubs:
        c = c["clubs"]
        return render(request, "secy_landing_page.html", {"clubs": c["aabhaschopra.bt19ele"]})


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

        event_id = ""

        collection_name = db["events"]
        events = collection_name.find({})

        collection_name = db["societies"]
        clubs = collection_name.find({})
        
        for c in clubs:
            c = c["clubs"]

            for club in c:
                if club == club_name:
                    if len(c[club]) == 1:
                        event_id = club + str(2301)
                    else:
                        event_id_org = c[club][len(c[club]) - 1]["event_id"]
                        event_id = event_id_org[-2:]
                        event_id = int(event_id) + 1

                        if event_id < 10:
                            event_id = event_id_org[:-2] + "0" + str(event_id)

                        else:
                            event_id = event_id_org[:-2] + str(event_id)

                    new_event = {
                        "name": event_name,
                        "description": event_description,
                        "event_organization": organisersList,
                        "event_participation": participantsList,
                        "event_id": event_id,
                        "sanction": sanction,
                        "sponsorship": sponsorship,
                        "college_level": college_level,
                        "date": event_date
                    }

                    #Following 3 lines to be commented once 'events' collection is fully synced
                    c[club].append(new_event)
                    collection_name.update({"_id": ObjectId(ObjectIdClubs)}, {"clubs": c})
                    collection_name = db["events"]

                    for e in events:
                        e = e["events"]

                        e[event_id] = new_event
                        collection_name.update({"_id": ObjectId(ObjectIdEvents)}, {"events": e})
        
        collection_name = db["students"]
        students = collection_name.find({})

        for s in students:
            s = s["students"]

            for student in s:
                if organisersList.count(student["sid"]) > 0:
                    student["event_organization"].append(event_id)
                    collection_name.update({"_id": ObjectId(ObjectIdStudents)}, {"students": s})

                if participantsList.count(student["sid"]) > 0:
                    student["event_participation"].append(event_id)
                    collection_name.update({"_id": ObjectId(ObjectIdStudents)}, {"students": s})

    return redirect("/secy/")
