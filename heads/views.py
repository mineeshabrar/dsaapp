from django.shortcuts import render

# Create your views here.

def head_view_data(request):
    return render(request, 'head_view.html')