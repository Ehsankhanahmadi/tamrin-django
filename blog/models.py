from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    time = models.TimeField()