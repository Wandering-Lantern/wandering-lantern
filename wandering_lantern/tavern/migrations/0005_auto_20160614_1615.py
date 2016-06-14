# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tavern', '0004_auto_20160614_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_features',
            name='level',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')], default=1, max_length=256),
        ),
        migrations.AlterField(
            model_name='race_features',
            name='name',
            field=models.IntegerField(max_length=256),
        ),
    ]
