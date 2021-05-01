from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=50)
