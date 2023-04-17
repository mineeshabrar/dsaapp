from django.contrib import admin
from django.urls import path, include
from student.views import *
from heads.views import *
from authentication.views import *
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view),
    path('student/', student_view_data),  
    path('', include('social_django.urls', namespace='social')),
    path('logout/', logout_view),
]
