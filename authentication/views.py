from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from majorProject.conf import connection_string
from heads.views import isHead
from dsa.views import isDSA
from pymongo import MongoClient


client = MongoClient(connection_string)
db = client['dsaapp-db']


def login_view(request):
    list(messages.get_messages(request))
    if request.user.is_authenticated:
        print("user email: " + request.user.email)
        if isHead(request):
            return redirect('secy/')
        
        elif isDSA(request):
            return redirect('/dsa')
        
        else:
            return redirect('student/')
                        
    else:
        logout(request)
        return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    list(messages.get_messages(request))
    return redirect('/')