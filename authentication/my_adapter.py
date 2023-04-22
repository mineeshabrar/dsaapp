from django.shortcuts import render, redirect
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.http import HttpResponse
from allauth.exceptions import ImmediateHttpResponse

class MyAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        email_domain = sociallogin.user.email.split('@')[1].lower()
        if not email_domain == 'pec.edu.in':
            # raise ImmediateHttpResponse(HttpResponse(sociallogin.user.email + ' is not valid memeber of pec.edu.in'))
            return render(request, 'login.html', {"error": sociallogin.user.email + ' is not valid memeber of pec.edu.in'})
        else:
            pass