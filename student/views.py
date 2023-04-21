from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def student_view_data(request, name = None, sid = None, prof = None):
    return render(request, 'nav_bar_student.html', {'name': name, 'sid' : sid, 'prof' :prof})

