from django.shortcuts import render
from .models import Tag, ProjectImage, Project

def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    context = {'projects': projects, 'tags': tags}
    return render(request, "home.html", context)

def contact(request):
    return render(request, "contact.html")

def project(request, id):
    return render(request, "project.html")



