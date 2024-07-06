from django.contrib import admin
from .models import Student, People

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
    

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'age', 'id']
    list_filter = ['city', 'age']
    search_fields = ['name']
    ordering = ['name']
    verbose_name_plural = 'Peoples'
    verbose_name = 'People'
    app_label = 'checkapi'
    show_facets = admin.ShowFacets.ALWAYS

