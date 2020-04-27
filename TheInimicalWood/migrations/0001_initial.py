# Generated by Django 3.0.5 on 2020-04-22 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_class', models.PositiveSmallIntegerField(choices=[(0, 'Knight'), (1, 'Archer'), (2, 'Sorcerer')], default=0)),
                ('attack_dmg', models.PositiveSmallIntegerField(default=10)),
                ('defence', models.PositiveSmallIntegerField(default=10)),
                ('hp', models.PositiveSmallIntegerField(default=100)),
                ('mana', models.PositiveSmallIntegerField(default=50)),
                ('stamina', models.PositiveSmallIntegerField(default=100)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='Avatars')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('hero_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='TheInimicalWood.Hero')),
                ('name', models.CharField(blank=True, max_length=20, unique=True)),
            ],
            bases=('TheInimicalWood.hero',),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('category', models.PositiveSmallIntegerField(choices=[(0, 'Others'), (1, 'Sword'), (2, 'Bow'), (3, 'Wand'), (4, 'Leather'), (5, 'Bow'), (6, 'Sorcerer robe'), (9, 'Consumables')], default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('price', models.PositiveSmallIntegerField(default=1)),
                ('bonus_attack_dmg', models.PositiveSmallIntegerField(default=0)),
                ('bonus_defence', models.PositiveSmallIntegerField(default=0)),
                ('bonus_hp', models.PositiveSmallIntegerField(default=0)),
                ('bonus_mana', models.PositiveSmallIntegerField(default=0)),
                ('bonus_stamina', models.PositiveSmallIntegerField(default=0)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheInimicalWood.Hero')),
            ],
        ),
    ]
