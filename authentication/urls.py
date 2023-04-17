from django.contrib import admin
from django.urls import path, include
from authentication.views import *

urlpatterns = [
    path('', login_view),
    path('logout/', logout_view)
]
