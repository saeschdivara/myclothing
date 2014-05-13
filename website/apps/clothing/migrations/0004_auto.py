# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field clothing_time on 'Clothing'
        m2m_table_name = db.shorten_name(u'clothing_clothing_clothing_time')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('clothing', models.ForeignKey(orm['clothing.clothing'], null=False)),
            ('clothingtime', models.ForeignKey(orm['clothing.clothingtime'], null=False))
        ))
        db.create_unique(m2m_table_name, ['clothing_id', 'clothingtime_id'])


    def backwards(self, orm):
        # Removing M2M table for field clothing_time on 'Clothing'
        db.delete_table(db.shorten_name(u'clothing_clothing_clothing_time'))


    models = {
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