from django.contrib import admin
from .models import JobPost

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'job_type', 'posted_on')
    search_fields = ('title', 'location')
    list_filter = ('job_type', 'posted_on')
