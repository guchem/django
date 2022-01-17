from django.db import models



class Todo(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=80)
    due_date = models.DateTimeField()
    