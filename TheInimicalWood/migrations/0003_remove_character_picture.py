# Generated by Django 3.0.5 on 2020-04-29 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TheInimicalWood', '0002_character_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='picture',
        ),
    ]
