from django.db import models

# Create your models here.
class Registeredusers(models.Model):
    username = models.CharField(max_length=50, null= True)
    firstname = models.CharField(max_length=50, null= True)
    lastname = models.CharField(max_length=50, null= True)
    email = models.EmailField(max_length=100, null= True)
    password = models.CharField(max_length=50, null= True)

    def __str__(self): # to display the username in the database
        return self.username

    class Meta:
        db_table = "Registeredusers"




class Adminusers(models.Model):
    username = models.CharField(max_length=50, null= True)
    firstname = models.CharField(max_length=50, null= True)
    lastname = models.CharField(max_length=50, null= True)
    email = models.EmailField(max_length=100, null= True)
    password = models.CharField(max_length=50, null= True)

    def __str__(self): # to display the username in the database
        return self.username

    class Meta:
        db_table = "Adminusers"


