# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-13 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_button', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buttonplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='aldryn_button_buttonplugin', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='buttonplugin',
            name='file',
            field=filer.fields.file.FilerFileField(blank=True, help_text='A file has priority over a phone number.', null=True, on_delete=django.db.models.deletion.PROTECT, to='filer.File', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='buttonplugin',
            name='target',
            field=models.CharField(blank=True, choices=[('', 'same window'), ('_blank', 'new window'), ('_parent', 'parent window'), ('_top', 'topmost frame')], max_length=100, verbose_name='target'),
        ),
    ]
