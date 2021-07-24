# Generated by Django 3.2.5 on 2021-07-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colonization_project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='registerd',
            new_name='registered',
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='username',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
