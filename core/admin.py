from django.contrib import admin

# Register your models here.
from core.models import Grade, Subject, Room, Report

admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Room)
admin.site.register(Report)
