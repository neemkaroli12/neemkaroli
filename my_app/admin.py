from django.contrib import admin
from .models import JobPost

# admin.py में ये confirm करें:
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_type', 'location', 'salary')  # salary add करें
