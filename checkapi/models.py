from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    grade = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'student'
        ordering = ['name']
        verbose_name_plural = 'Students'
        verbose_name = 'Student'
        app_label = 'checkapi'
        
    