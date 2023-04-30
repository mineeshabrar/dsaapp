from django.shortcuts import render, redirect
from components.conf import db
from datetime import date


def isDSA(request):
    collection_name = db["dsa_email"]

    dsa_emails = collection_name.find({})
    for dsa_email in dsa_emails:
        dsa_email = dsa_email["emails"]

        if request.user.email in dsa_email:
            return True

        else:
            return False


def dsa_add_event(request):
    return render(request, "add_event.html")


def view_student_list(request, year, branch):
    collection_name = db["students"]
    students = collection_name.find({})

    students_grouped = []
    for student in students:
        if str(int("20" + student["sid"][:2]) + 4) == year and (student["branch"] == branch or branch == "all"):
            students_grouped.append(student)      
    
    return render(request, "view_student_list.html", {"students_grouped": students_grouped, "branch": branch, "year": year})


def view_all_clubs(request):
    collection_name = db["societies"]
    clubs = collection_name.find({})

    return render(request, "view_all_clubs.html", {"clubs": clubs})


def students_grouped(request):
    collection_name = db["students"]
    students = collection_name.find({})

    years = set()
    branches = set()
    for student in students:
        student_year = int("20" + student["sid"][:2]) + 4
        years.add(student_year)
        branches.add(student["branch"])

    return render(request, "students_grouped.html", {"years": years, "branches": branches})    


def dsa_view(request):
    return render(request, "dsa_landing_page.html")