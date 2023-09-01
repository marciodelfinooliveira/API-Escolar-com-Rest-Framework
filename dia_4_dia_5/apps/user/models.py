from django.db import models
#from apps.todo.models import Task

class User(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
       
#   task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
        
    def __stg__(self):
        return self.name
