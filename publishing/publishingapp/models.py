from django.db import models
from django.utils import timezone
# Create your models here.


class author(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=11)
    passport = models.CharField(max_length=10)
    mail = models.CharField(max_length=50)


class publishing(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=11)
    mail = models.CharField(max_length=50)


class staff(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=11)
    passport = models.CharField(max_length=10)
    mail = models.CharField(max_length=50)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    priority = models.CharField(max_length=1,default='1')


class contract(models.Model):
    contractDate = models.DateField(default=timezone.now)
    circulation = models.IntegerField(default=0)
    format = models.CharField(max_length=50)
    volume = models.IntegerField(default=0)
    dateExecution = models.DateField(default=timezone.now)
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE)
    publishing_id = models.ForeignKey(publishing, on_delete=models.CASCADE)
    author_id = models.ForeignKey(author, on_delete=models.CASCADE)

