# Generated by Django 4.2 on 2023-04-23 23:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("task_log", "0003_plan_plansteps_artifact"),
        ("agents", "0002_agent_agent_class_path"),
    ]

    operations = [
        migrations.CreateModel(
            name="Chat",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "agents",
                    models.ManyToManyField(related_name="chats", to="agents.agent"),
                ),
                (
                    "artifacts",
                    models.ManyToManyField(
                        related_name="chats", to="task_log.artifact"
                    ),
                ),
                (
                    "lead",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="leading_chats",
                        to="agents.agent",
                    ),
                ),
                (
                    "resources",
                    models.ManyToManyField(related_name="chats", to="agents.resource"),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="leading_chats",
                        to="task_log.task",
                    ),
                ),
                (
                    "tasks",
                    models.ManyToManyField(related_name="chats", to="task_log.task"),
                ),
            ],
        ),
    ]
