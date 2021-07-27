# Generated by Django 3.2.5 on 2021-07-25 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colonization_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='colonization_project.person'),
        ),
    ]
