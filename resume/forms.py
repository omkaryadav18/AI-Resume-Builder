from django import forms
#from django.forms import modelformset_factory
from .models import Resume
class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['full_name', 'email', 'phone', 'summary', 'education', 'experience', 'certifications', 'achievements', 'skills', 'template']
        job_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}), label="Paste Job Description")

# class JobDescriptionForm(forms.Form):
#     job_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 6}), label="Paste Job Description")
