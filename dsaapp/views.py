from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, Attendance

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('secretary_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            error_message = 'Invalid login credentials'
    else:
        error_message = ''
    return render(request, 'login.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        roll_number = request.POST['roll_number']

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        student = Student.objects.create(user=user, roll_number=roll_number, email=email, phone_number=phone_number)

        return redirect('login')
    else:
        return render(request, 'signup.html')


@login_required(login_url='login')
def student_dashboard(request):
    student = request.user.student
    return render(request, 'student_dashboard.html', {'student': student})


@login_required(login_url='login')
def secretary_dashboard(request):
    if not request.user.is_staff:
        return redirect('student_dashboard')
    students = Student.objects.all()
    if request.method == 'POST':
        for student in students:
            attendance = Attendance(student=student)
            if str(student.id) in request.POST:
                attendance.present = True
            attendance.save()
    return render(request, 'secretary_dashboard.html', {'students': students})


@login_required(login_url='login')
def mark_attendance(request):
    if not request.user.is_staff:
        return redirect('student_dashboard')
    students = Student.objects.all()
    attendance_list = []
    for student in students:
        attendance, created = Attendance.objects.get_or_create(student=student, date=date.today())
        attendance_list.append({'student': student, 'attendance': attendance})
    return render(request, 'mark_attendance.html', {'attendance_list': attendance_list})
