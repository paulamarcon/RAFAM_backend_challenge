# Generated by Django 4.1.7 on 2023-02-16 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends_lessons', '0002_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lessons',
            field=models.ManyToManyField(to='friends_lessons.lesson'),
        ),
    ]
