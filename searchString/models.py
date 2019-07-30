from django.db import models

# Create your models here.
class Searchword(models.Model):
    word = models.CharField(max_length = 500)
    occurance = models.BigIntegerField()
    
    def __str__(self):
        return self.word