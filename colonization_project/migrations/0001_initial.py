# Generated by Django 3.2.5 on 2021-07-24 16:52

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('guid', models.CharField(max_length=50, unique=True)),
                ('has_died', models.BooleanField(default=False)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('picture', models.ImageField(upload_to='')),
                ('age', models.IntegerField()),
                ('eye_color', models.CharField(max_length=12, null=True)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Others', 'Others')], max_length=6)),
                ('about', models.TextField()),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('greeting', models.TextField()),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='colonization_project.company')),
                ('friend', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='colonization_project.person')),
            ],
        ),
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_veg', to='colonization_project.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_fruits', to='colonization_project.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
