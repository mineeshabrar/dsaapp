from django.shortcuts import render, redirect
from pymongo import MongoClient
from majorProject.conf import connection_string
from bson import ObjectId

client = MongoClient(connection_string)
db = client['dsaapp-db']

def isHead(request):
    collection_name = db["head_email"]

    head_emails = collection_name.find({})
    for h in head_emails:
        h = h["emails"]

        if request.user.email in h:
            return True
        
        else:
            return False
        

def event_details(request, event_id):
    collection_name = db["student_societies"]

    clubs = collection_name.find({})
    for c in clubs:
        c = c['clubs']
    
    events = c["aabhaschopra.bt19ele"]
    for event in events:
        if event["event_id"] == event_id:
            return render(request, 'event_view.html', {"event": event})


def secy_add_event(request):
    return render(request, 'add_event.html')

def view_proficiency(request):

    #
    prof = "aabhaschopra.bt19ele" 
    #
    client = MongoClient(connection_string)
        
    db = client['dsaapp-db']
    collection_name = db["student_student"]

    students = collection_name.find({})

    for s in students:
            s = s['students']

            for student in s:
                if(student['prof'] == prof):
                    return render(request, 'view_proficiency.html', {"student": student})

    return render(request, 'view_proficiency.html', {"student": student})
    
    # return render(request, 'view_proficiency.html')

def secy_view(request):
    collection_name = db["student_societies"]

    clubs = collection_name.find({})
    for c in clubs:
        c = c['clubs']
        return render(request, 'secy_landing_page.html', {"clubs" : c["aabhaschopra.bt19ele"]})
        # return render(request, 'secy_home_page.html')


def secy_add_event_data (request):
    if request.method == 'POST':
        #club_name = request.user.email.split('@')[0]
        club_name = "aabhaschopra.bt19ele"
        event_name = request.POST['EventName']
        event_description = request.POST['EventDescription']
        sanction = request.POST['CollegeSanction']
        sponsorship = request.POST['Sponsorship']
        college_level = request.POST['College']

        collection_name = db["student_societies"]

        clubs = collection_name.find({})

        for c in clubs:
            c = c['clubs']

            for club in c:
                if(club == club_name):
                    event_id = ""
                    if(len(c[club]) == 1):
                        event_id = club + str(2301)
                    else:
                        event_id_org = c[club][len(c[club]) - 1]['event_id']
                        event_id = event_id_org[-2:]
                        event_id = int(event_id) + 1

                        if(event_id < 10):
                            event_id = event_id_org[:-2] + "0" + str(event_id)

                        else:
                            event_id = event_id_org[:-2] + str(event_id)
                    
                    new_event = {
                        "name": event_name,
                        "description": event_description,
                        "event_organization": [
                         "19105115",
                        "19105118"
                         ],
                         "event_participation": [
                          "19105123",
                          "19105113"
                          ],
                        "event_id": event_id,
                        "sanction": sanction,
                        "sponsorship": sponsorship,
                        "college_level": college_level,
                    }

                    print(new_event)

                    c[club].append(new_event)
                    collection_name.update({"_id": ObjectId("643a2f1c3cf4f996659f0737")}, {"clubs": c})

                    break
                    #db.collection_names.updateOne({club_name}, {'$push' : new_event})
        
    return redirect('/secy/')
            