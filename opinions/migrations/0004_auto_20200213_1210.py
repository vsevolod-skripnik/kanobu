# Generated by Django 3.0.3 on 2020-02-13 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('persons', '0001_initial'),
        ('opinions', '0003_auto_20200213_0604'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='opinion',
            unique_together={('content_type', 'object_id', 'owner')},
        ),
    ]
