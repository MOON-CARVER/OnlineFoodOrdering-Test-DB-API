# Generated by Django 4.1.3 on 2024-12-02 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='cuisine_type',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='opening_hours',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='website_url',
        ),
    ]
