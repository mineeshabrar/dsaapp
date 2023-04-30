from django.contrib import admin
from django.urls import path, include, re_path
from student.views import *
from authentication.views import *
from heads.views import *
from dsa.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view),
    path('student/', student_view_data),
    path('student/<str:sid>/', student_final_view_data),
    path('accounts/', include("allauth.urls")),
    path('secy/<str:club_name>', secy_view),
    path('secy/add_event/', secy_add_event),
    path('secy/proficiency_list/', proficiency_list),
    path('secy/<str:club_name>/<str:event_id>', event_details),
    path('secy/<str:club_name>/<str:event_id>/<str:role>/', event_details),
    path('secy/saveData/', secy_add_event_data, name='saveAddEventData'),
    path('dsa/', dsa_view),
    path('dsa/<str:event_id>', event_details),
    path('dsa/add_event/', dsa_add_event),
    path('dsa/<str:year>/<str:branch>', view_student_list),
    path('student/<str:sid>/<str:role>/', student_final_view_data),
    re_path(r'^.*logout\/$', logout_view)
]
