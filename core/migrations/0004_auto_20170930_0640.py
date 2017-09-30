# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170930_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseinfo',
            name='ItemDescription',
            field=models.CharField(default='SOME STRING', max_length=300),
        ),
        migrations.AddField(
            model_name='purchaseinfo',
            name='ItemType',
            field=models.CharField(choices=[('S', 'Services'), ('G', 'Goods')], default='SOME STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='purchaseinfo',
            name='VendorName',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
    ]
