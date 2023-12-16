from django.shortcuts import render, redirect
from .models import Education, SkillLanguage, Projects, Experiences, Skill


# Create your views here.

def linkedin_redirect(request):
    return redirect('https://www.linkedin.com/in/adithya-rajendran/')


def github_redirect(request):
    return redirect('https://github.com/Adithya-Rajendran')


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def projects(request):
    projects = Projects.objects.all()
    return render(request, 'projects.html', {
        'projects': projects,
    })


def resume(request):
    educations = Education.objects.all()
    languages = SkillLanguage.objects.all()
    experiences = Experiences.objects.all()
    skills = Skill.objects.all()

    return render(request, 'resume.html', {
        'educations': educations,
        'languages': languages,
        'experiences': experiences,
        'skills': skills,
    })
