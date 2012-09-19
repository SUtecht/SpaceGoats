# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Article.approved'
        db.add_column('demo_article', 'approved', self.gf('django.db.models.fields.CharField')(default='Y', max_length=1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Article.approved'
        db.delete_column('demo_article', 'approved')


    models = {
        'demo.article': {
            'Meta': {'object_name': 'Article'},
            'approved': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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
