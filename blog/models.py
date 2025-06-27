from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    time = models.TimeField()
    img = models.ImageField(null=True,upload_to="blogimg")

    def __str__(self):
        return self.title