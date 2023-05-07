from django.shortcuts import render, redirect
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib import messages
from allauth.exceptions import ImmediateHttpResponse


class MyAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        email_domain = sociallogin.user.email.split("@")[1].lower()
        if not email_domain == "pec.edu.in":
            messages.error(request, "Please login with pec.edu.in")
            raise ImmediateHttpResponse(redirect("/"))
        else:
            pass
