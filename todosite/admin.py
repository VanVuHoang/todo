from django.contrib import admin
from .models import Task
from django.contrib.auth.models import PermissionsMixin

# Register your models here

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'contents', 'date']
    list_filter = ['date']
    search_fields = ['title']

admin.site.register(Task, TaskAdmin)


