from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    name_text = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name_text

class Action(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name_text = models.CharField(max_length=30)
    action_text = models.CharField(max_length=255)
    action_date = models.DateTimeField('date published')
    
class Automatable(models.Model):
    name_text = models.CharField(max_length=255)
    state_text = models.CharField(max_length=255)
