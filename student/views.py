from django.shortcuts import render, redirect
from pymongo import MongoClient
from majorProject.conf import connection_string


def student_view_data(request):
    client = MongoClient(connection_string)
        
    db = client['dsaapp-db']
    collection_name = db["student_student"]

    students = collection_name.find({})

    for s in students:
        s = s['students']

        for student in s:
            if(student['email'] == request.user.email):
                name = student['name']
                sid = student['sid']
                prof = student['prof']
                # return redirect(f'student/{name}/{sid}/{prof}')
                return render(request, 'student_home_page.html', {"name": name, "sid": sid, "prof": prof,})
            
    return render(request, 'student_home_page.html', {"name": None, "sid": None, "prof": None,})
