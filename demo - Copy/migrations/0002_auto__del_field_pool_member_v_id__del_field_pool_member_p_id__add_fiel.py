# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Pool_Member.v_id'
        db.delete_column('demo_pool_member', 'v_id_id')

        # Deleting field 'Pool_Member.p_id'
        db.delete_column('demo_pool_member', 'p_id_id')

        # Adding field 'Pool_Member.voter'
        db.add_column('demo_pool_member', 'voter', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['demo.Voter']), keep_default=False)

        # Adding field 'Pool_Member.pool'
        db.add_column('demo_pool_member', 'pool', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['demo.Pool']), keep_default=False)

        # Deleting field 'Transaction.e_id'
        db.delete_column('demo_transaction', 'e_id_id')

        # Deleting field 'Transaction.pm_id'
        db.delete_column('demo_transaction', 'pm_id_id')

        # Adding field 'Transaction.pool_member'
        db.add_column('demo_transaction', 'pool_member', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['demo.Pool_Member']), keep_default=False)

        # Adding field 'Transaction.event'
        db.add_column('demo_transaction', 'event', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['demo.Event']), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Pool_Member.v_id'
        db.add_column('demo_pool_member', 'v_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['demo.Voter']), keep_default=False)

        # Adding field 'Pool_Member.p_id'
        db.add_column('demo_pool_member', 'p_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['demo.Pool']), keep_default=False)

        # Deleting field 'Pool_Member.voter'
        db.delete_column('demo_pool_member', 'voter_id')

        # Deleting field 'Pool_Member.pool'
        db.delete_column('demo_pool_member', 'pool_id')

        # Adding field 'Transaction.e_id'
        db.add_column('demo_transaction', 'e_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['demo.Event']), keep_default=False)

        # Adding field 'Transaction.pm_id'
        db.add_column('demo_transaction', 'pm_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['demo.Pool_Member']), keep_default=False)

        # Deleting field 'Transaction.pool_member'
        db.delete_column('demo_transaction', 'pool_member_id')

        # Deleting field 'Transaction.event'
        db.delete_column('demo_transaction', 'event_id')


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
