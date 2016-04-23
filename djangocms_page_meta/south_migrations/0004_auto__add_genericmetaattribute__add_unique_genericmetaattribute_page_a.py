# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GenericMetaAttribute'
        db.create_table('djangocms_page_meta_genericmetaattribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['djangocms_page_meta.PageMeta'], related_name='extra', null=True)),
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, to=orm['djangocms_page_meta.TitleMeta'], related_name='extra', null=True)),
            ('attribute', self.gf('django.db.models.fields.CharField')(default='name', max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('djangocms_page_meta', ['GenericMetaAttribute'])

        # Adding unique constraint on 'GenericMetaAttribute', fields ['page', 'attribute', 'name', 'value']
        db.create_unique('djangocms_page_meta_genericmetaattribute', ['page_id', 'attribute', 'name', 'value'])

        # Adding unique constraint on 'GenericMetaAttribute', fields ['title', 'attribute', 'name', 'value']
        db.create_unique('djangocms_page_meta_genericmetaattribute', ['title_id', 'attribute', 'name', 'value'])


    def backwards(self, orm):
        # Removing unique constraint on 'GenericMetaAttribute', fields ['title', 'attribute', 'name', 'value']
        db.delete_unique('djangocms_page_meta_genericmetaattribute', ['title_id', 'attribute', 'name', 'value'])

        # Removing unique constraint on 'GenericMetaAttribute', fields ['page', 'attribute', 'name', 'value']
        db.delete_unique('djangocms_page_meta_genericmetaattribute', ['page_id', 'attribute', 'name', 'value'])

        # Deleting model 'GenericMetaAttribute'
        db.delete_table('djangocms_page_meta_genericmetaattribute')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.page': {
            'Meta': {'object_name': 'Page', 'unique_together': "(('publisher_is_draft', 'site', 'application_namespace'), ('reverse_id', 'site', 'publisher_is_draft'))", 'ordering': "('path',)"},
            'application_namespace': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'application_urls': ('django.db.models.fields.CharField', [], {'blank': 'True', 'db_index': 'True', 'null': 'True', 'max_length': '200'}),
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_home': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True', 'default': 'None', 'db_index': 'True', 'null': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'blank': 'True', 'db_index': 'True', 'null': 'True', 'max_length': '80'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['cms.Page']", 'related_name': "'children'", 'null': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'db_index': 'True', 'null': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'db_index': 'True', 'null': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'to': "orm['cms.Page']", 'unique': 'True', 'null': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'blank': 'True', 'db_index': 'True', 'null': 'True', 'max_length': '40'}),
            'revision_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'djangocms_pages'", 'to': "orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'INHERIT'", 'max_length': '100'}),
            'xframe_options': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'})
        },
        'cms.title': {
            'Meta': {'object_name': 'Title', 'unique_together': "(('language', 'page'),)"},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'has_url_overwrite': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15'}),
            'menu_title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True', 'max_length': '155'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'title_set'", 'to': "orm['cms.Page']"}),
            'page_title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'path': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'to': "orm['cms.Title']", 'unique': 'True', 'null': 'True'}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'redirect': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '2048'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'djangocms_page_meta.genericmetaattribute': {
            'Meta': {'object_name': 'GenericMetaAttribute', 'unique_together': "(('page', 'attribute', 'name', 'value'), ('title', 'attribute', 'name', 'value'))"},
            'attribute': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['djangocms_page_meta.PageMeta']", 'related_name': "'extra'", 'null': 'True'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['djangocms_page_meta.TitleMeta']", 'related_name': "'extra'", 'null': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        'djangocms_page_meta.pagemeta': {
            'Meta': {'object_name': 'PageMeta'},
            'extended_object': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.Page']", 'unique': 'True'}),
            'fb_pages': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '255'}),
            'gplus_author': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '255'}),
            'gplus_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['filer.File']", 'related_name': "'djangocms_page_meta_page'", 'null': 'True'}),
            'og_app_id': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '255'}),
            'og_author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['auth.User']", 'null': 'True'}),
            'og_author_fbid': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '16'}),
            'og_author_url': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '255'}),
            'og_publisher': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '255'}),
            'og_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'public_extension': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'draft_extension'", 'to': "orm['djangocms_page_meta.PageMeta']", 'unique': 'True', 'null': 'True'}),
            'twitter_author': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '255'}),
            'twitter_site': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '255'}),
            'twitter_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'})
        },
        'djangocms_page_meta.titlemeta': {
            'Meta': {'object_name': 'TitleMeta'},
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '400'}),
            'extended_object': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.Title']", 'unique': 'True'}),
            'gplus_description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['filer.File']", 'related_name': "'djangocms_page_meta_title'", 'null': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '400'}),
            'og_description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '400'}),
            'public_extension': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'draft_extension'", 'to': "orm['djangocms_page_meta.TitleMeta']", 'unique': 'True', 'null': 'True'}),
            'twitter_description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '140'})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['filer.Folder']", 'related_name': "'all_files'", 'null': 'True'}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '255'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'owned_files'", 'null': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_filer.file_set+'", 'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'sha1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '40'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'})
        },
        'filer.folder': {
            'Meta': {'object_name': 'Folder', 'unique_together': "(('parent', 'name'),)", 'ordering': "('name',)"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'filer_owned_folders'", 'null': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['filer.Folder']", 'related_name': "'children'", 'null': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'ordering': "('domain',)", 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['djangocms_page_meta']