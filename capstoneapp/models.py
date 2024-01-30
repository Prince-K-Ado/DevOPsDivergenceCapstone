from django.db import models

# Create your models here.

class Capstoneapp(models.Model):
    index = models.CharField(max_length=255, primary_key=True)
    Movie = models.CharField(max_length=255)
    Distr = models.CharField(max_length=255)
    Gross = models.CharField(max_length=255)
    date = models.CharField(max_length=255)

    def __str__(self):
        return self.Movie + ' ' + self.Distr