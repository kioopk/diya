# Generated by Django 5.0.6 on 2024-06-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0003_alter_order_books"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order", name="books", field=models.TextField(blank=True),
        ),
    ]
