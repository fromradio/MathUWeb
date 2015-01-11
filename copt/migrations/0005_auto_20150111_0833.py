# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import copt.models


class Migration(migrations.Migration):

    dependencies = [
        ('copt', '0004_chapter_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='project',
            field=models.ForeignKey(default=copt.models.get_project, to='home.Project'),
            preserve_default=True,
        ),
    ]
