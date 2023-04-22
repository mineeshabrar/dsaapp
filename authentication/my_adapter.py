from django.shortcuts import render, redirect
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.http import HttpResponse
from allauth.exceptions import ImmediateHttpResponse
from django.contrib import messages

class MyAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        email_domain = sociallogin.user.email.split('@')[1].lower()
        if not email_domain == 'pec.edu.in':
            messages.error(request, "Document deleted.")
            # raise ImmediateHttpResponse(HttpResponse(sociallogin.user.email + ' is not valid memeber of pec.edu.in'))
            return render(request, 'login.html')
        else:
            pass