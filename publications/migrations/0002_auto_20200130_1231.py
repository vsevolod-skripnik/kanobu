# Generated by Django 2.2 on 2020-01-30 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
    ]
