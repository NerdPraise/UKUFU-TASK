# Generated by Django 3.2.5 on 2021-07-27 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colonization_project', '0003_auto_20210727_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='friend',
            new_name='friends',
        ),
    ]
