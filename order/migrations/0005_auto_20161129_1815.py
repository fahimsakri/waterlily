# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 18:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0004_order_serial_no'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='order',
            unique_together=set([('serial_no', 'user')]),
        ),
    ]
