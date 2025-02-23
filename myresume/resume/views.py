from django.shortcuts import render
from resume.models import *
# Create your views here.
def index(request):
    degrees = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    about = Bio.objects.all()[0]
    languages = Language.objects.all()
    profile = Profile.objects.all()[0]
    context = {
        'degrees' : degrees,
        'skills' : skills,
        'projects' : projects,
        'about' : about,
        'languages' : languages,
        'peofile': profile
    }
    return render(request, 'index.html', context)