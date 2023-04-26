from django.shortcuts import render, redirect
from pymongo import MongoClient
from django.contrib import messages
from allauth.exceptions import ImmediateHttpResponse
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from majorProject.conf import connection_string


def student_final_view_data(request, sid):
    client = MongoClient(connection_string)
        
    db = client['dsaapp-db']
    collection_name = db["student_student"]

    students = collection_name.find({})

    for s in students:
            s = s['students']

            for student in s:
                if(student['sid'] == sid):
                    return render(request, 'student_home_page.html', {"student": student})

    return render(request, 'student_landing_page.html', {"student": student})


def student_view_data(request):
        client = MongoClient(connection_string)
        
        db = client['dsaapp-db']
        collection_name = db["student_student"]

        students = collection_name.find({})

        for s in students:
            s = s['students']

            for student in s:
                if(student['email'] == request.user.email):
                    sid = student['sid']
                    return redirect(f'{sid}/')

            messages.error(request, "{} is not authenticated. Please contact DSA office.".format(request.user.email)) 
            logout(request)
            return HttpResponseRedirect('/')