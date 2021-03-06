# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tavern', '0007_auto_20160614_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='hit_die',
            field=models.CharField(choices=[('D4', 'D4'), ('D6', 'D6'), ('D8', 'D8'), ('D12', 'D12')], default='D6', max_length=256),
        ),
        migrations.AlterField(
            model_name='class',
            name='martial_melee_prof',
            field=models.ManyToManyField(to='tavern.MartialMelee'),
        ),
        migrations.AlterField(
            model_name='class',
            name='martial_ranged_prof',
            field=models.ManyToManyField(to='tavern.MartialRanged'),
        ),
        migrations.AlterField(
            model_name='class',
            name='simple_ranged_prof',
            field=models.ManyToManyField(to='tavern.SimpleRanged'),
        ),
        migrations.AlterField(
            model_name='class',
            name='skill_prof',
            field=models.ManyToManyField(to='tavern.SkillProficiencies'),
        ),
        migrations.AlterField(
            model_name='meleeweapon',
            name='hit_die',
            field=models.CharField(choices=[('D4', 'D4'), ('D6', 'D6'), ('D8', 'D8'), ('D12', 'D12')], max_length=256),
        ),
        migrations.AlterField(
            model_name='meleeweapon',
            name='properties',
            field=models.ManyToManyField(to='tavern.WeaponProperties'),
        ),
        migrations.AlterField(
            model_name='race',
            name='martial_melee_prof',
            field=models.ManyToManyField(to='tavern.MartialMelee'),
        ),
        migrations.AlterField(
            model_name='race',
            name='martial_ranged_prof',
            field=models.ManyToManyField(to='tavern.MartialRanged'),
        ),
        migrations.AlterField(
            model_name='race',
            name='simple_ranged_prof',
            field=models.ManyToManyField(to='tavern.SimpleRanged'),
        ),
        migrations.AlterField(
            model_name='race',
            name='skill_prof',
            field=models.ManyToManyField(to='tavern.SkillProficiencies'),
        ),
        migrations.AlterField(
            model_name='rangedweapon',
            name='hit_die',
            field=models.CharField(choices=[('D4', 'D4'), ('D6', 'D6'), ('D8', 'D8'), ('D12', 'D12')], max_length=256),
        ),
        migrations.AlterField(
            model_name='rangedweapon',
            name='properties',
            field=models.ManyToManyField(to='tavern.WeaponProperties'),
        ),
    ]
