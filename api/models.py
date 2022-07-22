from django.db import models

# Create your models here.

# '''creating class '''

class Api(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    img = models.ImageField()
    desc = models.CharField(max_length=250)

    def __str__(self):
        return self.title