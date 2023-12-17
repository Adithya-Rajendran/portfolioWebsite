from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Education, SkillLanguage, Projects, Experiences, Skill
from .forms import ContactForm


# Create your views here.
def linkedin_redirect(request):
    return redirect('https://www.linkedin.com/in/adithya-rajendran/')


def github_redirect(request):
    return redirect('https://github.com/Adithya-Rajendran')


def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print("form is valid")
            messages.success(request, 'Your message was successfully submitted!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
    })


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
