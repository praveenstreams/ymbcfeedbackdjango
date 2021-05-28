from django.db import models

# Create your models here.
class student(models.Model):

    name=models.CharField(max_length=20)
    number=models.BigIntegerField()
    password=models.CharField(max_length=20)


class feedback_oncourse(models.Model):

    number=models.IntegerField(max_length=20,default=0)
    department=models.CharField(max_length=20)
    sem=models.IntegerField(max_length=10)
    content=models.CharField(max_length=20)
    coverage=models.CharField(max_length=20)
    application=models.CharField(max_length=20)
    value=models.CharField(max_length=20)
    clarity=models.CharField(max_length=20)
    metirial=models.CharField(max_length=20)
    effort=models.CharField(max_length=20)
    overall=models.CharField(max_length=20)


class feedback_onfaculty(models.Model):
    number = models.IntegerField(max_length=20,default=0)
    department=models.CharField(max_length=20)
    sem=models.IntegerField(max_length=10)
    teacher=models.CharField(max_length=20)
    knowledge=models.CharField(max_length=20)
    communication=models.CharField(max_length=20)
    Commitment=models.CharField(max_length=20)
    interest=models.CharField(max_length=20)
    integratingskill=models.CharField(max_length=20)
    integratecontent=models.CharField(max_length=20)
    accessibility=models.CharField(max_length=20)
    cordination=models.CharField(max_length=20)
    provision=models.CharField(max_length=20)
    overall=models.CharField(max_length=20)


