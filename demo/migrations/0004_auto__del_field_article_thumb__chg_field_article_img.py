# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Article.thumb'
        db.delete_column('demo_article', 'thumb')

        # Changing field 'Article.img'
        db.alter_column('demo_article', 'img', self.gf('goatnails.db.models.ImageWithThumbsField')(max_length=100))


    def backwards(self, orm):
        
        # Adding field 'Article.thumb'
        db.add_column('demo_article', 'thumb', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Changing field 'Article.img'
        db.alter_column('demo_article', 'img', self.gf('django.db.models.fields.files.ImageField')(max_length=100))


    models = {
        'demo.article': {
            'Meta': {'object_name': 'Article'},
            'approved': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Player']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('goatnails.db.models.ImageWithThumbsField', [], {'max_length': '100'}),
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
