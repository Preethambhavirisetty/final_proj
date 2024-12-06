# Generated by Django 5.0.5 on 2024-05-06 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("service_posts", "0001_initial"),
        ("service_users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Questions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(blank=True, unique=True)),
                ("body", models.TextField(blank=True)),
                ("is_answered", models.BooleanField(default=False)),
                ("is_favorite", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("last_activity", models.DateTimeField(auto_now_add=True)),
                ("view_count", models.IntegerField(default=0)),
                ("answer_count", models.IntegerField(default=0)),
                ("tags", models.ManyToManyField(to="service_posts.tags")),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="service_users.users",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Questions",
            },
        ),
    ]