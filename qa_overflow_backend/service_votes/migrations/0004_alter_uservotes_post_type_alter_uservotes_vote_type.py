# Generated by Django 5.0.5 on 2024-05-11 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service_votes", "0003_alter_uservotes_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uservotes",
            name="post_type",
            field=models.CharField(
                choices=[("Question", "question"), ("Answer", "answer")], max_length=25
            ),
        ),
        migrations.AlterField(
            model_name="uservotes",
            name="vote_type",
            field=models.CharField(
                choices=[("Upvote", "upvote"), ("Downvote", "downvote")], max_length=25
            ),
        ),
    ]
