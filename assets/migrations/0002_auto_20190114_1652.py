# Generated by Django 2.1.4 on 2019-01-14 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventlog',
            old_name='user',
            new_name='User',
        ),
    ]