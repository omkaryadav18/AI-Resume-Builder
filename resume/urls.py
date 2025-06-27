from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_resume, name='create_resume'),
    path('preview/<int:resume_id>/', views.preview_resume, name='preview_resume'),
    path('download/<int:resume_id>/', views.download_resume_pdf, name='download_resume_pdf'),
    path('match/<int:resume_id>/', views.match_resume_to_job, name='match_resume_to_job'),
    path('generate-from-job/', views.generate_resume_from_job, name='generate_from_job'),
    path('generate-resume/', views.generate_resume_from_job, name='generate_resume'),

]
