# Generated by Django 4.1.3 on 2024-12-18 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_remove_customeruser_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='customer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]
