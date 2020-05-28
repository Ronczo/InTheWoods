# Generated by Django 3.0.5 on 2020-05-18 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheInimicalWood', '0022_auto_20200518_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='current_stamina',
            field=models.PositiveSmallIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='item',
            name='bonus_current_stamina',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
