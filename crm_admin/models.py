from django.db import models
from django.contrib.auth.hashers import check_password as django_check_password

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Store securely (hashing)
    # Add any other fields as needed

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def check_password(self, raw_password):
        return django_check_password(raw_password, self.password)
