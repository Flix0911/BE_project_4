from django.db import models
from django.contrib.auth.models import User

# Plate model
class Plate(models.Model):
    # plate will have a name
    title = models.CharField(max_length=100)
    # plate will have a size
    size = models.CharField(max_length=100)
    # how it is related to the user ~ FK is linking a user with data that belongs to user
    # CASCADE means if ID1 is deleted, everything with it will be deleted
    # User.plates ~ will give all plates
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="plates")
    
    def __str__(self):
        return self.title
    
    
# Cup model
class Cup(models.Model):
    # cup will have a name
    title = models.CharField(max_length=100)
    # cup will have a size
    size = models.CharField(max_length=100)
    # how it is related to the user
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cups")
    
    def __str__(self):
        return self.title