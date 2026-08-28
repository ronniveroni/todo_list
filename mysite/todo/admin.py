from django.contrib import admin
from .models import Task,Tag

class TaskAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'status']

# Register your models here.
admin.site.register(Task,TaskAdmin)
admin.site.register(Tag)