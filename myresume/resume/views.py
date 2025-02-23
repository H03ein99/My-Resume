from django.shortcuts import render
from resume.models import *
# Create your views here.
def index(request):
    degrees = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    about = Bio.objects.all()[0]
    languages = Language.objects.all()
    context = {
        'degrees' : degrees,
        'skills' : skills,
        'projects' : projects,
        'about' : about,
        'languages' : languages,
    }
    return render(request, 'index.html', context)