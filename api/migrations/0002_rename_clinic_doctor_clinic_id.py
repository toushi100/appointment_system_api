# Generated by Django 4.1.3 on 2022-11-19 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='clinic',
            new_name='clinic_id',
        ),
    ]
