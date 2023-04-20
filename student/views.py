from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def student_view_data(request):
    return render(request, 'nav_bar_student.html')

