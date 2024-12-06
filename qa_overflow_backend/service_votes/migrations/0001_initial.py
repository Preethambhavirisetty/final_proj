# Generated by Django 5.0.5 on 2024-05-10 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("service_posts", "0008_alter_commentvotes_unique_together"),
        ("service_users", "0005_alter_users_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserVotes",
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
                (
                    "post_type",
                    models.CharField(
                        choices=[("question", "Question"), ("answer", "Answer")],
                        max_length=25,
                    ),
                ),
                (
                    "vote_type",
                    models.CharField(
                        choices=[("upvote", "Upvote"), ("downvote", "Downvote")],
                        max_length=25,
                    ),
                ),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="service_posts.posts",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="service_users.users",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "UserVotes",
            },
        ),
    ]