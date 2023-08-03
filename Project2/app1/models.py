from django.db import models
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    price=models.IntegerField()
    pdf=models.FileField(upload_to='book/pdf')
    cover=models.ImageField(upload_to='book/img',null=True,blank=True)
    def __str__(self):
      return self.title


class Person(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    age=models.IntegerField()
    def __str__(self):
        return self.name


class Myuser(AbstractUser):
    place=models.CharField(max_length=30)
    phone=models.IntegerField()
    is_admin=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
    is_person=models.BooleanField(default=False)

# class Customuser(AbstractUser):


