from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User,related_name="user",primary_key=True,on_delete=models.CASCADE)
    is_google_auth = models.BooleanField(default=False)
