from django.db import models
from django.contrib.auth.models import User

# Create your models here.



    

class Pharma(models.Model):
    name = models.CharField(max_length = 150)
    contact = models.CharField(max_length = 100)
    add_by = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length = 150)
    vote = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name
    
    
    

