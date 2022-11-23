from django.db import models
'''we need to import  the following for our User class'''
from django.contrib.auth.models import User
from django.db.models import Model

# Create your models here.
class task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class meta:
    ordering = ['complete']




