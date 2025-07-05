from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task, ContextEntry, Category

admin.site.register(Task)
admin.site.register(ContextEntry)
admin.site.register(Category)
