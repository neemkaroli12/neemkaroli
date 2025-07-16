from django.db import models

JOB_TYPE_CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
)

class JobPost(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    salary = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
        
class JobPostForm(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    description = models.TextField()
