from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_height = models.PositiveIntegerField(blank=True, editable=False, default=400)
    image_width = models.PositiveIntegerField(blank=True, editable=False, default=300)
    image_url = models.ImageField(upload_to='uploads/', height_field='image_height', width_field='image_width')

    def __str__(self):
        return self.name


class Education(models.Model):
    institution = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    degree_type = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.institution} ({self.start_year} - {self.end_year})"


class Experience(models.Model):
    job_title = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.employer} ({self.start_year} - {self.end_year})"


class SkillLanguage(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
