# Generated by Django 3.0.5 on 2020-05-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheInimicalWood', '0009_auto_20200507_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
