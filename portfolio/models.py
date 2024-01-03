from django.db import models


class AboutMe(models.Model):
    passion = models.TextField()
    about = models.TextField()
    summary = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True, default='images/profile.png')

    def save(self, *args, **kwargs):
        # Ensure there is only one instance in the database
        if AboutMe.objects.exists() and not self.pk:
            # If an instance already exists, update its fields
            existing_instance = AboutMe.objects.first()
            existing_instance.passion = self.passion
            existing_instance.about = self.about
            existing_instance.summary = self.summary
            if self.image is not None:
                existing_instance.image = self.image
            existing_instance.save()
            return existing_instance
        return super().save(*args, **kwargs)

    def __str__(self):
        return "About Me"

    class Meta:
        verbose_name_plural = "About Me"


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.ImageField(upload_to='projects/', height_field='image_height', width_field='image_width')

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
