from django.shortcuts import render
from resume.models import *
# Create your views here.
def index(request):
    education = Education.objects.all()
    for degree in education:
        degree.start_year = degree.start_date.year
        degree.end_year = degree.end_date.year
    skills = Skill.objects.all()
    for skill in skills:
        skill.percentage = skill.level_to_percentage()
    projects = Project.objects.all()
    about = Bio.objects.all()[0]
    languages = Language.objects.all()
    profile = Profile.objects.all()[0]
    project_counter = Project.objects.count()
    context = {
        'education' : education,
        'skills' : skills,
        'projects' : projects,
        'about' : about,
        'languages' : languages,
        'profile': profile,
        'project_counter': project_counter,
    }
    return render(request, 'index.html', context)