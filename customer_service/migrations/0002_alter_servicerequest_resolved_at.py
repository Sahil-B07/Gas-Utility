# Generated by Django 4.2.5 on 2024-07-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer_service", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicerequest",
            name="resolved_at",
            field=models.DateTimeField(blank=True, default="Not Yet", null=True),
        ),
    ]
