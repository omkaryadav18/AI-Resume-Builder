from django.db import models
from django.contrib.auth.models import User

'''TEMPLATE_CHOICES = [
    ('classic', 'Classic'),
    ('professional', 'Professional'),
    ('modern', 'Modern'),
    ('elegant', 'Elegant'),
]'''
#dummy = models.BooleanField(default=False)

class Resume(models.Model):
    TEMPLATE_CHOICES = [
        ('classic', 'Classic'),
        ('professional', 'Professional'),
        ('modern', 'Modern'),
        ('elegant', 'Elegant'),
    ]
    template_choice = models.CharField(max_length=20, choices=TEMPLATE_CHOICES, default='classic')


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    summary = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    certifications = models.TextField(default='No certifications yet')  # Add default to avoid future issues
    achievements = models.TextField(default='No achievements yet')
    template = models.CharField(max_length=20, choices=TEMPLATE_CHOICES, default='classic')

    def __str__(self):
        return f"{self.full_name}'s Resume"

'''class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    school = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_present = models.BooleanField(default=False)
    description = models.TextField(blank=True)

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_present = models.BooleanField(default=False)
    description = models.TextField(blank=True)'''