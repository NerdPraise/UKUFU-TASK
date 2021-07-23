# Generated by Django 3.2.5 on 2021-07-23 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colonization_project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='company',
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='colonization_project.company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='eye_color',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Others', 'Others')], max_length=6),
        ),
    ]
