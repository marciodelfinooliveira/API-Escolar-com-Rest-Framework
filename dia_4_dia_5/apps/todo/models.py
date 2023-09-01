from django.db import models
from apps.user.models import User


class Task(models.Model):

    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __stg__(self):
        return self.name
