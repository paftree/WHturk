# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 08:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20160218_0749'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together=set([('system_A', 'system_B'), ('system_B', 'system_A')]),
        ),
    ]
