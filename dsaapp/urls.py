from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('secretary/', views.secretary_dashboard, name='secretary_dashboard'),
    path('mark-attendance/<int:student_id>/', views.mark_attendance, name='mark_attendance'),
]
