# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ffxiv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='ilvl',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=False,
        ),
    ]
