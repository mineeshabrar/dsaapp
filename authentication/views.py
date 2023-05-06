from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from components.get_club_name import get_club_name

from heads.views import isHead
from dsa.views import isDSA


def login_view(request):
    list(messages.get_messages(request))
    if request.user.is_authenticated:
        print("user email: " + request.user.email)
        if isHead(request):
            club_name = get_club_name(request.user.email)
            return redirect(f"secy/{club_name}")

        elif isDSA(request):
            return redirect("dsa/")

        else:
            return redirect("student/")

    else:
        logout(request)
        return render(request, "login_page.html")


@login_required
def logout_view(request):
    logout(request)
    list(messages.get_messages(request))
    return redirect("/")
