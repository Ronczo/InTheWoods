# Generated by Django 3.0.5 on 2020-05-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheInimicalWood', '0008_remove_item_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]
