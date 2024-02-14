from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField("Username", max_length=30, unique=True)
    password = models.CharField("passWord", max_length=32)
    create_time = models.DateTimeField("createTime", auto_now_add=True)
    updated_time = models.DateTimeField("updatedTime", auto_now=True)

    def __str__(self):
        return "USER" + self.username
