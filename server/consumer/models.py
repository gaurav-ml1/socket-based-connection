from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=250, null=True, blank=True)
    device_number = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.device_name


