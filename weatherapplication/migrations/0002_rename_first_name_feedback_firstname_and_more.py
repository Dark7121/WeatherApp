# Generated by Django 4.2.2 on 2023-08-22 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapplication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
