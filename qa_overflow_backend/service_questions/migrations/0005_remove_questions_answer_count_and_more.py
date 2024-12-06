# Generated by Django 5.0.5 on 2024-05-07 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service_questions", "0004_rename_downvote_questions_downvotes_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="questions",
            name="answer_count",
        ),
        migrations.RemoveField(
            model_name="questions",
            name="view_count",
        ),
        migrations.AddField(
            model_name="questions",
            name="viewers",
            field=models.TextField(default=""),
        ),
    ]