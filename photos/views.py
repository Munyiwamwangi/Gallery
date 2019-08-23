from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import dt
from .models import Editor, Category, Image


# Create your views here.
def welcome(request):
    return render(request, "welcome.html")
    pass