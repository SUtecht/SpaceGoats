# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Character'
        db.create_table('demo_character', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo.Player'])),
            ('server', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('demo', ['Character'])

        # Adding model 'Player'
        db.create_table('demo_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
        ))
        db.send_create_signal('demo', ['Player'])

        # Adding model 'Event'
        db.create_table('demo_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('begin', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('demo', ['Event'])

        # Adding M2M table for field attendees on 'Event'
        db.create_table('demo_event_attendees', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['demo.event'], null=False)),
            ('character', models.ForeignKey(orm['demo.character'], null=False))
        ))
        db.create_unique('demo_event_attendees', ['event_id', 'character_id'])

        # Adding model 'Rank'
        db.create_table('demo_rank', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('demo', ['Rank'])

        # Adding model 'Article'
        db.create_table('demo_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo.Player'])),
        ))
        db.send_create_signal('demo', ['Article'])


    def backwards(self, orm):
        
        # Deleting model 'Character'
        db.delete_table('demo_character')

        # Deleting model 'Player'
        db.delete_table('demo_player')

        # Deleting model 'Event'
        db.delete_table('demo_event')

        # Removing M2M table for field attendees on 'Event'
        db.delete_table('demo_event_attendees')

        # Deleting model 'Rank'
        db.delete_table('demo_rank')

        # Deleting model 'Article'
        db.delete_table('demo_article')


    models = {
        'demo.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Player']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'demo.character': {
            'Meta': {'object_name': 'Character'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Player']"}),
            'server': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'demo.event': {
            'Meta': {'object_name': 'Event'},
            'attendees': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['demo.Character']", 'null': 'True', 'blank': 'True'}),
            'begin': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'demo.player': {
            'Meta': {'object_name': 'Player'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'demo.rank': {
            'Meta': {'object_name': 'Rank'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['demo']
