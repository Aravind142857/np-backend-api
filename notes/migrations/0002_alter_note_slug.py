# Generated by Django 4.2.4 on 2023-08-31 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
