# Generated by Django 2.2 on 2020-01-30 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('persons', '0001_initial'),
        ('publications', '0002_auto_20200130_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person', verbose_name='Person'),
        ),
        migrations.AddField(
            model_name='comment',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Publication', verbose_name='Publication'),
        ),
    ]
