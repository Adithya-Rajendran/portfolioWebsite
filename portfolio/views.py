from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm
from .models import Education, SkillLanguage, Project, Experience, Skill, AboutMe
from decouple import config


# Create your views here.
def linkedin_redirect(request):
    return redirect('https://www.linkedin.com/in/adithya-rajendran/')


def github_redirect(request):
    return redirect('https://github.com/Adithya-Rajendran')


def home(request):
    aboutme = AboutMe.objects.first()
    return render(request, 'index.html', {
        'aboutme': aboutme
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Your message was successfully submitted!')
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = str(form.cleaned_data['phone'])
            content = form.cleaned_data['message']

            html_message = render_to_string('extra/_email_template.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'content': content,
            })

            message = ('Contact Form Submission\n'
                       'Name: {}\n'
                       'Email: {}\n'
                       'Phone: {}\n'
                       'Message: {}').format(name, email, phone, content)

            email_user = config('EMAIL_HOST_USER', default='')
            my_emails_str = config('MY_EMAILS', default='')
            my_emails = [email.strip() for email in my_emails_str.split(',')]

            send_mail(
                'Contact Form for My Website',
                message,
                email_user,
                my_emails,
                fail_silently=False,
                html_message=html_message,
            )
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
    })


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects,
    })


def resume(request):
    educations = Education.objects.all()
    languages = SkillLanguage.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()

    return render(request, 'resume.html', {
        'educations': educations,
        'languages': languages,
        'experiences': experiences,
        'skills': skills,
    })
