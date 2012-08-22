# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Voter'
        db.create_table('demo_voter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mname', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('lname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254, blank=True)),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('work_phone', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('cell_phone', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('loc_code', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('demo', ['Voter'])

        # Adding model 'Event'
        db.create_table('demo_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('begin', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('completed', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('demo', ['Event'])

        # Adding model 'Term'
        db.create_table('demo_term', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('begin', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('demo', ['Term'])

        # Adding model 'Pool'
        db.create_table('demo_pool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo.Term'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parent_pool', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo.Pool'], null=True, blank=True)),
        ))
        db.send_create_signal('demo', ['Pool'])

        # Adding model 'Pool_Member'
        db.create_table('demo_pool_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('v_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo.Voter'])),
            ('p_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo.Pool'])),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('demo', ['Pool_Member'])

        # Adding model 'Transaction'
        db.create_table('demo_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pm_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo.Pool_Member'])),
            ('e_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo.Event'])),
            ('payment_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('processed', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('demo', ['Transaction'])


    def backwards(self, orm):
        
        # Deleting model 'Voter'
        db.delete_table('demo_voter')

        # Deleting model 'Event'
        db.delete_table('demo_event')

        # Deleting model 'Term'
        db.delete_table('demo_term')

        # Deleting model 'Pool'
        db.delete_table('demo_pool')

        # Deleting model 'Pool_Member'
        db.delete_table('demo_pool_member')

        # Deleting model 'Transaction'
        db.delete_table('demo_transaction')


    models = {
        'demo.event': {
            'Meta': {'object_name': 'Event'},
            'begin': ('django.db.models.fields.DateTimeField', [], {}),
            'completed': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
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
            'p_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Pool']"}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'v_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Voter']"})
        },
        'demo.term': {
            'Meta': {'object_name': 'Term'},
            'begin': ('django.db.models.fields.DateTimeField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'demo.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'e_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'pm_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['demo.Pool_Member']"}),
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
