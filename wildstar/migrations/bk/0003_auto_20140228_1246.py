# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffxiv', '0002_level_ilvl'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='ilvl',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='level',
            name='ilvl',
        ),
    ]
