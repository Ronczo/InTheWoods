# Generated by Django 3.0.5 on 2020-04-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheInimicalWood', '0004_item_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Others'), (1, 'Sword'), (2, 'Bow'), (3, 'Wand'), (4, 'Leather'), (5, 'Bow'), (6, 'Sorcerer robe'), (7, 'Consumables')], default=0),
        ),
    ]
