# Generated by Django 3.0.5 on 2020-06-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheInimicalWood', '0025_auto_20200531_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='mission',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
