from django.db import models

# Create your models here.

class Sport(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def _str_(self):
        return self.name
    