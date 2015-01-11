# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150108_0706'),
        ('copt', '0003_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='project',
            field=models.ForeignKey(default=0, to='home.Project'),
            preserve_default=True,
        ),
    ]
