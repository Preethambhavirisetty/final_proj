# Generated by Django 5.0.5 on 2024-05-11 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service_questions", "0013_alter_questions_last_activity"),
        ("service_users", "0005_alter_users_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questions",
            name="last_activity",
            field=models.CharField(
                blank=True,
                default=datetime.datetime(
                    2024, 5, 11, 17, 58, 30, 75433, tzinfo=datetime.timezone.utc
                ),
                max_length=100,
            ),
        ),
        migrations.RemoveField(
            model_name="questions",
            name="viewers",
        ),
        migrations.AddField(
            model_name="questions",
            name="viewers",
            field=models.ManyToManyField(
                related_name="viewers", to="service_users.users"
            ),
        ),
    ]