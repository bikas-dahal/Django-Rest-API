from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class People(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name

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
        

# Signal for creating token for new user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
    