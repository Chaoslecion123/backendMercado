from django.contrib import admin
from .models import Schedule
# Register your models here.

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass
