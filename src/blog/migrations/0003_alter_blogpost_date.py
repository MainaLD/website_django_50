# Generated by Django 5.0.2 on 2024-02-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_blogpost_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
    ]