from django.db import models
from django.contrib.auth.models import User, AbstractUser



# class User(AbstractUser):
#     name = models.CharField(max_length = 200, null = True)
#     email = models.EmailField(unique=True, null=True)
    


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Task(models.Model):
    list = models.ForeignKey(List, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
