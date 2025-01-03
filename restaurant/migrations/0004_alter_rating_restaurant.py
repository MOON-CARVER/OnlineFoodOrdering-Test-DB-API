# Generated by Django 4.1.3 on 2024-12-03 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0003_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="restaurant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ratings",
                to="restaurant.restaurantuser",
            ),
        ),
    ]