from django.contrib import admin
from .models import Education, SkillLanguage, Projects, Experiences, Skill

# Register your models here.
admin.site.register(Education)
admin.site.register(SkillLanguage)
admin.site.register(Projects)
admin.site.register(Experiences)
admin.site.register(Skill)
