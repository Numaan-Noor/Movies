from django.db import models

# Create your models here.

class Movies(models.Model):
    Name = models.CharField(max_length=500)
    file = models.FileField()

    def __str__(self):
        return "{}".format(self.Name)
