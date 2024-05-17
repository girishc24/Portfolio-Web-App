from django.shortcuts import render
from .models import Tag, ProjectImage, Project

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def project(request, id):
    return render(request, "project.html")



