from django.db import models

class Lesson(models.Model):
    name = models.CharField(max_length=255)

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    lessons = models.ManyToManyField(Lesson)
    friends = models.ManyToManyField("self")
