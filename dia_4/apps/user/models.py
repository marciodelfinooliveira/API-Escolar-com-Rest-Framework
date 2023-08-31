from django.db import models

class User(models.Model):

    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
        
    def __stg__(self):
        return self.name
