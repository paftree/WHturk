# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20160218_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tracker.System'),
        ),
        migrations.AlterField(
            model_name='character',
            name='ship',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
