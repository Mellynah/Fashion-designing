# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-01 14:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bags_name', models.CharField(max_length=200)),
                ('bags_color', models.CharField(max_length=200)),
                ('bags_size', models.CharField(max_length=200)),
                ('bag_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('bags_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]