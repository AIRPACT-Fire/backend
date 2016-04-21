# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 00:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convos', '0002_auto_20160403_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, default='')),
                ('convoPage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convos.convoPage')),
            ],
        ),
    ]