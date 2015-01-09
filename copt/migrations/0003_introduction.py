# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('copt', '0002_item_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=5000)),
                ('chapter', models.ForeignKey(to='copt.Chapter')),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
    ]
