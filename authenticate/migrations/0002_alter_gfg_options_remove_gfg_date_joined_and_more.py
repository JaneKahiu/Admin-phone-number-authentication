# Generated by Django 5.0.7 on 2024-08-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gfg',
            options={},
        ),
        migrations.RemoveField(
            model_name='gfg',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='gfg',
            name='email',
        ),
        migrations.RemoveField(
            model_name='gfg',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='gfg',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='gfg',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='gfg',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='gfg',
            name='username',
        ),
        migrations.AlterField(
            model_name='gfg',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
