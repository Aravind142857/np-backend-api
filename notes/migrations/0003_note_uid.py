# Generated by Django 4.2.4 on 2023-09-01 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0002_alter_note_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="uid",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
