# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field pools on 'Event'
        db.create_table('demo_event_pools', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['demo.event'], null=False)),
            ('pool', models.ForeignKey(orm['demo.pool'], null=False))
        ))
        db.create_unique('demo_event_pools', ['event_id', 'pool_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field pools on 'Event'
        db.delete_table('demo_event_pools')


    models = {
        'demo.event': {
            'Meta': {'object_name': 'Event'},
            'begin': ('django.db.models.fields.DateTimeField', [], {}),
            'completed': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pools': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['demo.Pool']", 'symmetrical': 'False'})
        },
        'demo.pool': {
            'Meta': {'object_name': 'Pool'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_pool': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Pool']", 'null': 'True', 'blank': 'True'}),
            'term': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Term']"})
        },
        'demo.pool_member': {
            'Meta': {'object_name': 'Pool_Member'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pool': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Pool']"}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'voter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Voter']"})
        },
        'demo.term': {
            'Meta': {'object_name': 'Term'},
            'begin': ('django.db.models.fields.DateTimeField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'demo.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'pool_member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Pool_Member']"}),
            'processed': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'demo.voter': {
            'Meta': {'object_name': 'Voter'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'loc_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'mname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['demo']
