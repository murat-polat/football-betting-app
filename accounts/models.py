from django.db import models
from django.contrib.auth.models import User


## User model
class User(models.Model):

    username = models.CharField(max_length= 150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

    def __repr__(self):
        return self.username, self.first_name, self.last_name, self.email
