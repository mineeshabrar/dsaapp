from django.shortcuts import render, redirect
from components.conf import db
from datetime import date
import pandas as pd
import xlsxwriter
from django.http import HttpResponse
import io
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.cache import cache
@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def download_excel(request,club_name):
    if(request.session["role"]=='dsa'):

# Currently all this does is, find the details of all ACM-CSS students (Hard-coded) and downloads the excel file.
        data = db["students"].find({"prof":club_name})

        df = pd.DataFrame(list(data))
        output = io.BytesIO()

        # Use pandas to write the DataFrame to the BytesIO stream as an Excel file
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)
        writer.close()
        output.seek(0)

        # Set the appropriate HTTP response headers
        response = HttpResponse(output, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="students.xlsx"'

        return response
    else:
        return redirect("/")


def isDSA(request):
    collection_name = db["dsa_email"]

    dsa_emails = collection_name.find({})
    for dsa_email in dsa_emails:
        dsa_email = dsa_email["emails"]

        if request.user.email in dsa_email:
            return True

        return False

@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def dsa_add_event(request):
    if(request.session["role"]=='dsa'):
        return render(request, "add_event.html",{"role":"dsa"})
    else:
        return redirect("/")

@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def view_student_list(request, year, branch):
    if(request.session["role"]=='dsa'):
        collection_name = db["students"]
        students = collection_name.find({})

        students_grouped = []
        for student in students:
            if str(int("20" + student["sid"][:2]) + 4) == year and (student["branch"] == branch or branch == "all"):
                students_grouped.append(student)      
        
        return render(request, "view_student_list.html", {"students_grouped": students_grouped, "branch": branch, "year": year})
    else:
        return redirect("/")

@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def view_all_clubs(request):
    if(request.session["role"]=='dsa'):
        collection_name = db["societies"]
        clubs = collection_name.find({})

        return render(request, "view_all_clubs.html", {"clubs": clubs})
    else:
        return redirect("/")
@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def students_grouped(request):
    if(request.session["role"]=='dsa'):
        collection_name = db["students"]
        students = collection_name.find({})

        years = set()
        branches = set()
        for student in students:
            student_year = int("20" + student["sid"][:2]) + 4
            years.add(student_year)
            branches.add(student["branch"])

        return render(request, "students_grouped.html", {"years": years, "branches": branches}) 
    else:
        return redirect("/")   

@login_required(login_url='/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def dsa_view(request):
    print(dict(request.session))
    if(dict(request.session)["role"]=='dsa'):
        return render(request, "dsa_landing_page.html")
    else:
        return redirect("/")
    
