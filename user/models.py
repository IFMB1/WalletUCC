from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    web_site = models.CharField(max_length=255, blank=True)