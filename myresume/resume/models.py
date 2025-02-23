from django.db import models

# Create your models here.
class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.proficiency})"

class Project(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField()
    github_url = models.URLField()

    def __str__(self):
        return f"{self.name}"


class Bio(models.Model):
    bio_text = models.TextField()

    def __str__(self):
        return "Bio Information"