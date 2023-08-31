from django.db import models

class Task(models.Model):

    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date = models.DateField()
    
    def __stg__(self):
        return self.name
