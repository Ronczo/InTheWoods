# Generated by Django 3.0.5 on 2020-04-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheInimicalWood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='picture',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
