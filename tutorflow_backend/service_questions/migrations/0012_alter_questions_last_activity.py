# Generated by Django 5.0.5 on 2024-05-11 00:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service_questions", "0011_alter_questions_last_activity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questions",
            name="last_activity",
            field=models.CharField(
                blank=True,
                default=datetime.datetime(
                    2024, 5, 11, 0, 59, 13, 161706, tzinfo=datetime.timezone.utc
                ),
                max_length=100,
            ),
        ),
    ]