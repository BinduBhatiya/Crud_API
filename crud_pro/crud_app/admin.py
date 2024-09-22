from django.contrib import admin
from .models import studentmodel

# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display = ['name', 'roll', 'city']

admin.site.register(studentmodel,studentadmin)
