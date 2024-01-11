from django.db import models


class AboutMe(models.Model):
    passion = models.TextField()
    about = models.TextField()
    summary = models.TextField()
    image_url = models.URLField(max_length=400)
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
    sort = models.IntegerField(default=100)
    image_url = models.URLField(max_length=400)

    def __str__(self):
        return self.name


class Education(models.Model):
    institution = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    degree_type = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.institution} ({self.start_date.year} - {self.end_date.year if self.end_date else 'Present'})"


class Experience(models.Model):
    job_title = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.employer} ({self.start_date.year} - {self.end_date.year if self.end_date else 'Present'})"


class SkillLanguage(models.Model):
    name = models.CharField(max_length=255)
    priority_choices = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    priority = models.IntegerField(choices=priority_choices, default=2)

    def __str__(self):
        return f"{self.name} - Priority: {self.get_priority_display()}"


class Skill(models.Model):
    name = models.CharField(max_length=255)
    priority_choices = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    priority = models.IntegerField(choices=priority_choices, default=2)

    def __str__(self):
        return f"{self.name} - Priority: {self.get_priority_display()}"
