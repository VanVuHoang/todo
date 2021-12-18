from django.contrib import admin
from .models import Task

# Register your models here

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'contents', 'date', 'check']
    list_filter = ['date', 'check']
    search_fields = ['title', 'check']

admin.site.register(Task, TaskAdmin)
