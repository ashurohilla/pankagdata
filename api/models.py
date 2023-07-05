from django.db import models

# Create your models here.

class Knowledge_base(models.Model):
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='images/')
    contact = models.CharField(max_length=100, null=True, default=None)
    website = models.CharField(max_length=100, null = True, default=None)
    address = models.CharField(max_length=150, null =True, default=None)
    location = models.CharField(max_length = 150, null= True ,default=None)
    Gender = models.CharField(max_length=160, null=True, default=None)
    
    def __str__(self):
        return f'{self.name}'
