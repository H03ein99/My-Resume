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
    proficiency = models.CharField(max_length=50,
                                   choices=[
                                       ('Advanced', 'Advanced'),
                                       ('Intermediate', 'Intermediate'),
                                       ('Beginner', 'Beginner'),
                                   ])

    def level_to_percentage(self):
        level_mapping = {
            'Advanced': 99,
            'Intermediate': 66,
            'Beginner': 33
        }
        return level_mapping.get(self.proficiency, 0)    


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
    
class Language(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50,
                                   choices = [
                                                ('Native', 'Native'),
                                                ('Fluent', 'Fluent'),
                                                ('Advanced', 'Advanced'),
                                                ('Intermediate', 'Intermediate'),
                                                ('Beginner', 'Beginner')])

        
    def __str__(self):
        return f"{self.name} - {self.proficiency}"
    
class Profile(models.Model):
    birthday = models.DateField()
    first_name = models.CharField(max_length=100)    
    last_name = models.CharField(max_length=100) 
    website = models.URLField()
    city = models.CharField(max_length=250)
    age = models.IntegerField()
    degree = models.CharField(max_length=200)
    email = models.EmailField()
    about = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"