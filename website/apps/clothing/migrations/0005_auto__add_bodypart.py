# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BodyPart'
        db.create_table(u'clothing_bodypart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal('clothing', ['BodyPart'])

        # Adding M2M table for field clothing on 'BodyPart'
        m2m_table_name = db.shorten_name(u'clothing_bodypart_clothing')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bodypart', models.ForeignKey(orm['clothing.bodypart'], null=False)),
            ('clothing', models.ForeignKey(orm['clothing.clothing'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bodypart_id', 'clothing_id'])


    def backwards(self, orm):
        # Deleting model 'BodyPart'
        db.delete_table(u'clothing_bodypart')

        # Removing M2M table for field clothing on 'BodyPart'
        db.delete_table(db.shorten_name(u'clothing_bodypart_clothing'))


    models = {
        'clothing.bodypart': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'BodyPart'},
            'clothing': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'body_parts'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['clothing.Clothing']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        'clothing.clothing': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Clothing'},
            'clothing_time': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'clothes'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['clothing.ClothingTime']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'name'", 'overwrite': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        'clothing.clothingtime': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'ClothingTime'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'name'", 'overwrite': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        }
    }

    complete_apps = ['clothing']