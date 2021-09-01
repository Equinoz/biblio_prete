from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	address = models.CharField(blank=True, max_length=100)
	zip_code = models.CharField(blank=True, max_length=5)
	city = models.CharField(blank=True, max_length=50)