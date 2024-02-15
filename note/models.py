from django.db import models

from user.models import User


# Create your models here.
class Note(models.Model):
    title = models.CharField('Title', max_length=30)

    content = models.TextField('Content')
    up_dated_time = models.DateTimeField("Updated_Time", auto_now=True)
    create_time = models.DateTimeField("Create_Time", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
