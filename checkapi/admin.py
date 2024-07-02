from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll', 'city', 'grade', 'id']
    list_filter = ['city', 'grade']
    search_fields = ['name']
    ordering = ['name']
    verbose_name_plural = 'Students'
    verbose_name = 'Student'
    app_label = 'checkapi'
    show_facets = admin.ShowFacets.ALWAYS
    


