# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='last_refresh',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 13, 33, 26, 784859)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='last_refresh_request',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 3, 13, 33, 34, 417067)),
            preserve_default=False,
        ),
    ]
