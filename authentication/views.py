from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from pymongo import MongoClient


def login_view(request):
    if request.user.is_authenticated:
        connection_string = "mongodb://localhost:27017/?retryWrites=true&w=majority"

        client = MongoClient(connection_string)
        db = client['dsaapp-db']
        collection_name = db["student_student"]

        students = collection_name.find({})

        # students is dictionary which has 2 elements { _id and students }
        for s in students:
            # s is the list of all students
            s = s['students']

            for student in s:
                if student['email'] == request.user.email:
                    name = student['name']
                    sid = student['sid']
                    prof = student['prof']
            
            
        return render(request, 'student_home_page.html', {'name': name, 'sid': sid, 'prof': prof})
    
    else:
        return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')