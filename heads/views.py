from django.shortcuts import render, redirect
from pymongo import MongoClient
from majorProject.conf import connection_string

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
    return redirect(request, 'event_view.html', {"event_id": event_id})


def secy_view(request):
    collection_name = db["student_societies"]

    clubs = collection_name.find({})
    for c in clubs:
        c = c['clubs']
        return render(request, 'secy_landing_page.html', {"clubs" : c["saasc"]})
