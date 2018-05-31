# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 10:52
from __future__ import unicode_literals

from django.db import migrations

from weblate.gitexport.models import get_export_url, SUPPORTED_VCS


def set_export_url(apps, schema_editor):
    Component = apps.get_model('trans', 'Component')
    matching = Component.objects.filter(
        vcs__in=SUPPORTED_VCS
    ).exclude(
        repo__startswith='weblate:/'
    )
    for component in matching:
        new_url = get_export_url(component)
        if component.git_export != new_url:
            component.git_export = new_url
            component.save()


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0069_source_screenshot'),
    ]

    run_before = [
        ('trans', '0131_auto_20180416_1610'),
    ]

    operations = [
        migrations.RunPython(
            set_export_url,
            reverse_code=set_export_url,
        )
    ]
