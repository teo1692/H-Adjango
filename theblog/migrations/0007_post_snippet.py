# Generated by Django 3.1.5 on 2021-01-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20210129_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above To Read Post', max_length=255),
        ),
    ]
