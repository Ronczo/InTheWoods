# Generated by Django 3.0.5 on 2020-05-12 18:05

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('TheInimicalWood', '0012_remove_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='backpack',
            field=jsonfield.fields.JSONField(default=None),
        ),
    ]
