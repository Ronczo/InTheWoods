# Generated by Django 3.0.5 on 2020-04-29 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TheInimicalWood', '0005_auto_20200429_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
    ]
