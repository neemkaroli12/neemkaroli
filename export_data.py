# export_data.py
import io
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # replace with your settings module
django.setup()

from django.core.management import call_command

with io.open("data.json", "w", encoding="utf8") as f:
    call_command("dumpdata", exclude=["auth.permission", "contenttypes"], indent=2, stdout=f)
