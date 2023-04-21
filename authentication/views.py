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
        # students is dictionary which has 2 elements { id and students }, students has a list of all students inside

        for stds in students:
            stds = stds['students']
            # stds now is the list of all students
            for student in stds:

                # student now goes through the whole list to look for data with that specific id 
                if student['email'] == request.user.email:
                    name = student['name']
                    sid = student['sid']
                    prof = student['prof']
                    return redirect(f'student/{name}/{sid}/{prof}')
                
        return render(request, 'login.html')
    
    else:
        logout(request)
        return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')