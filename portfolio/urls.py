from django.urls import path
from . import views


urlpatterns = [
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('linkedin/', views.linkedin_redirect, name='linkedin'),
    path('github/', views.github_redirect, name='github'),
    path("", views.home, name="home"),
]
