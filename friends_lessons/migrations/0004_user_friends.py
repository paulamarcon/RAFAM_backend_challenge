# Generated by Django 4.1.7 on 2023-02-16 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends_lessons', '0003_user_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(to='friends_lessons.user'),
        ),
    ]
