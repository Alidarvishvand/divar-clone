# Generated by Django 5.2.4 on 2025-07-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminpanel", "0003_adminsupportmessage_subject"),
    ]

    operations = [
        migrations.AddField(
            model_name="adminsupportmessage",
            name="is_answered",
            field=models.BooleanField(default=False),
        ),
    ]
