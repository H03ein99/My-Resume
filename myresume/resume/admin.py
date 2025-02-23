from django.contrib import admin
from resume.models import Education, Skill, Project, Bio, Language, Profile

# Register your models here.
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Bio)
admin.site.register(Language)
admin.site.register(Profile)