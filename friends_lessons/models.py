from django.db import models

class Lesson(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    lessons = models.ManyToManyField(Lesson)
    friends = models.ManyToManyField("self")

    def __str__(self):
        return self.firstname
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    