from django.shortcuts import render

# Create your views here.

def student_view_data(request):
    return render(request, 'student_home_page.html')

def log_out(request):
    return render(request, 'log_out.html')
