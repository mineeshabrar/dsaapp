from django.contrib import admin
from django.urls import path, include, re_path
from student.views import *
from authentication.views import *
from heads.views import *
from dsa.views import *

urlpatterns = [
    re_path(r"^.*logout\/$", logout_view),
    path("admin/", admin.site.urls),
    path("", login_view),
    path("student/", student_view_data),
    path("student/<str:sid>/", student_final_view_data),
    path("student/<str:sid>/organized_events/", student_final_view_data),
    path("student/<str:sid>/participated_events/", student_final_view_data),
    path("accounts/", include("allauth.urls")),
    path("secy/proficiency_list/<str:club_name>/", proficiency_list),
    path("secy/download_excel", download_prof),
    path("secy/saveData/", secy_add_event_data, name="saveAddEventData"),
    path("secy/<str:club_name>", secy_view),
    path("secy/<str:club_name>/add_event/", secy_add_event),
    path("secy/<str:club_name>/<str:event_id>/", event_details),
    path("dsa/", dsa_view),
    path("dsa/add_event/", dsa_add_event),
    path("dsa/download_excel/<str:club_name>/", download_excel),
    path("dsa/students_grouped/", students_grouped),
    path("dsa/view_all_clubs/", view_all_clubs),
    path("dsa/<str:event_id>/", event_details),
    path("dsa/<str:year>/<str:branch>/", view_student_list),
    path("dsa/deleteEvent/<str:club_name>/<str:event_id>/", delete_event, name="delete-event"),
]
