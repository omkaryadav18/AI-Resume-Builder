from django.http import HttpResponse
#from django.forms import modelformset_factory
import google.generativeai as genai
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm #JobDescriptionForm
from .models import Resume
from django.contrib.auth.decorators import login_required
from django.conf import settings

genai.configure(api_key = settings.GEMINI_API_KEY)

'''EducationFormSet = modelformset_factory(Education, fields=('degree', 'institution', 'year'), extra=1)
ExperienceFormSet = modelformset_factory(Experience, fields=('job_title', 'company', 'duration'), extra=1)
'''

@login_required
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()

            return redirect('preview_resume', resume_id=resume.id)
    
    else:
        form = ResumeForm()
    return render(request, 'resume/create_resume.html', {'form': form})

@login_required
def generate_resume_from_job(request):
    if request.method == 'POST':
        job_desc = request.POST.get('job_description')

        prompt = f"""
        Job Description:
        {job_desc}

        Create a professional resume draft based on the above job description. Output fields should be:
        - Full Name
        - Email
        - Phone
        - Summary
        - Skills (comma-separated)
        - Education (degree, institution, year)
        - Experience (job title, company, duration)

        Format as JSON with the following keys: full_name, email, phone, summary, skills, education, experience.
        """

        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

            import json, re

            # Clean and parse JSON
            json_data = re.search(r'{.*}', response.text, re.DOTALL)
            resume = json.loads(json_data.group()) if json_data else {}

            return render(request, 'resume/create_resume.html', {
                'form': ResumeForm(initial={
                    'full_name': resume.get('full_name'),
                    'email': resume.get('email'),
                    'phone': resume.get('phone'),
                    'summary': resume.get('summary'),
                    'skills': resume.get('skills'),
                    'education': resume.get('education'),
                    'experience':resume.get('experience'),
                    'certification': resume.get('certifications'),
                    'achievements': resume.get('achievements')
                }),
                # 'edu_formset': EducationFormSet(queryset=Education.objects.none(), initial=[
                #     edu for edu in resume_data.get('education', [])
                # ]),
                # 'exp_formset': ExperienceFormSet(queryset=Experience.objects.none(), initial=[
                #     exp for exp in resume_data.get('experience', [])
                # ])
            })
        except Exception as e:
            return HttpResponse(f"⚠️ Error generating resume: {str(e)}")

    else:
        form = ResumeForm()
    return render(request, 'resume/job_input.html', {'form': form})

@login_required
def preview_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)

    template_map = {
        'classic': 'resume/template_classic.html',
        'professional': 'resume/template_professional.html',
        'modern': 'resume/template_modern.html',
        'elegant': 'resume/template_elegant.html',
    }
    template_name = template_map.get(resume.template_choice, 'resume/template_classic.html')

    return render(request, template_name, {'resume': resume})

@login_required
def download_resume_pdf(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)

    template_map = {
        'classic': 'resume/template_classic.html',
        'professional': 'resume/template_professional.html',
        'modern': 'resume/template_modern.html',
        'elegant': 'resume/template_elegant.html',
    }
    template_name = template_map.get(resume.template_choice, 'resume/template_classic.html')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{resume.full_name}_resume.pdf"'

    template = get_template(template_name)
    html = template.render({'resume': resume})

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors while generating the PDF.')
    return response

@login_required
def match_resume_to_job(request, resume_id):
    if request.method == 'POST':
        job_desc = request.POST.get('job_description')
        resume = get_object_or_404(Resume, id=resume_id, user=request.user)

        prompt =f"""
        Resume:
        Name: {resume.full_name}
        Email: {resume.email}
        Phone: {resume.phone}
        Skills: {resume.skills}
        Education: {resume.education}
        Experience: {resume.experience}
        Certifications: {resume.certifications}
        Achievements: {resume.achievements}

        Job Description:
        {job_desc}

        Compare the resume with the job description.
        Task:
        1. Evaluate how well this resume fits the job.
        2. Give suggestions to improve the resume for this role.
        3. Highlight missing skills or experience.
        4. Output should be clear, bullet-pointed, and actionable.
        Give improvement suggestions"""

        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

            return render(request, 'resume/ai_suggestions.html', {
                'resume': resume,
                'job_description': job_desc,
                'ai_response': response.text
            })
        except Exception as e:
            return render(request, 'resume/ai_suggestions.html', {
                'resume': resume,
                'job_description': job_desc,
                'ai_response': f"⚠️ An error occurred while generating suggestions: {str(e)}"

            })
    return render(request, 'resume/job_description_form.html', {'resume_id':resume_id})


# @login_required
# def generate_resume_from_job(request):
#     if request.method == 'POST':
#         job_desc = request.POST.get('job_description')

#         prompt = f"""
#         Job Description:
#         {job_desc}

#         Create a professional resume draft based on the above job description. Output fields should be:
#         - Full Name
#         - Email
#         - Phone
#         - Summary
#         - Skills (comma-separated)
#         - Education (degree, institution, year)
#         - Experience (job title, company, duration)

#         Format as JSON with the following keys: full_name, email, phone, summary, skills, education, experience.
#         """

#         try:
#             model = genai.GenerativeModel("gemini-1.5-flash")
#             response = model.generate_content(prompt)

#             import json, re

#             # Clean and parse JSON
#             json_data = re.search(r'{.*}', response.text, re.DOTALL)
#             resume_data = json.loads(json_data.group()) if json_data else {}

#             return render(request, 'resume/create_resume.html', {
#                 'form': ResumeForm(initial={
#                     'full_name': resume_data.get('full_name'),
#                     'email': resume_data.get('email'),
#                     'phone': resume_data.get('phone'),
#                     'summary': resume_data.get('summary'),
#                     'skills': resume_data.get('skills'),
#                     'education': resume_data.get('education'),
#                     'experience':resume_data.get('experience'),
#                     'certification': resume_data.get('certifications'),
#                     'achievements': resume_data.get('achievements')
#                 }),
#                 # 'edu_formset': EducationFormSet(queryset=Education.objects.none(), initial=[
#                 #     edu for edu in resume_data.get('education', [])
#                 # ]),
#                 # 'exp_formset': ExperienceFormSet(queryset=Experience.objects.none(), initial=[
#                 #     exp for exp in resume_data.get('experience', [])
#                 # ])
#             })
#         except Exception as e:
#             return HttpResponse(f"⚠️ Error generating resume: {str(e)}")

#     return render(request, 'resume/job_input.html')
