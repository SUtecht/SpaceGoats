# encoding: utf8
from django.db import models, migrations
from django.conf import settings
import goatnails.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('abv', models.CharField(max_length=3)),
                ('icon', goatnails.db.models.ImageWithThumbsField(upload_to='uploads', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('creation_date', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('server', models.CharField(max_length=100)),
                ('picture', goatnails.db.models.ImageWithThumbsField(upload_to='uploads', blank=True)),
                ('lodestone_id', models.IntegerField(blank=True)),
                ('levels', models.ManyToManyField(to='ffxiv.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.ForeignKey(to='ffxiv.Character', to_field=u'id')),
                ('job', models.ForeignKey(to='ffxiv.Job', to_field=u'id')),
                ('level', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('caption', models.CharField(max_length=500, blank=True)),
                ('creation_date', models.DateField(auto_now=True)),
                ('image', goatnails.db.models.ImageWithThumbsField(upload_to='uploads', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
