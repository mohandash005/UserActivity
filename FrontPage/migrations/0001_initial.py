# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2020-03-28 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=120)),
                ('Mail', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=140)),
                ('Password', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='User_Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=140)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
            ],
        ),
    ]
