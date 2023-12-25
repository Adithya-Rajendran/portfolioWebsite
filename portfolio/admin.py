from django.contrib import admin

from .models import Education, SkillLanguage, Project, Experience, Skill, AboutMe

# Register your models here.
admin.site.register(Education)
admin.site.register(SkillLanguage)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(AboutMe)
