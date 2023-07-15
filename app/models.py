from django.db import models

# Create your models here.
class Movie(models.Model):
    
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    isActive = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.title