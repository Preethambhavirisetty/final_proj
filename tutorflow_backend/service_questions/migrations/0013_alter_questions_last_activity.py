# Generated by Django 5.0.5 on 2024-05-11 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service_questions", "0012_alter_questions_last_activity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questions",
            name="last_activity",
            field=models.CharField(
                blank=True,
                default=datetime.datetime(
                    2024, 5, 11, 1, 17, 36, 506299, tzinfo=datetime.timezone.utc
                ),
                max_length=100,
            ),
        ),
    ]