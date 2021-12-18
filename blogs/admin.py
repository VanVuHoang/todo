from django.contrib import admin
from .models import Post, CheckIn

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']

class CheckInAdmin(admin.ModelAdmin):
    list_display = ['check']
    list_filter = ['check']
    search_fields = ['check']

admin.site.register(Post, PostAdmin)
admin.site.register(CheckIn, CheckInAdmin)
