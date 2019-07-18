# Generated by Django 2.1.4 on 2018-12-08 21:02

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("utils", "0003_auto_20181112_2150"),
    ]

    operations = [
        migrations.CreateModel(
            name="ObjectChange",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True)),
                ("user_name", models.CharField(editable=False, max_length=150)),
                ("request_id", models.UUIDField(editable=False)),
                (
                    "action",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Created"), (2, "Updated"), (3, "Deleted")]
                    ),
                ),
                ("changed_object_id", models.PositiveIntegerField()),
                (
                    "related_object_id",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                ("object_repr", models.CharField(editable=False, max_length=256)),
                (
                    "object_data",
                    django.contrib.postgres.fields.jsonb.JSONField(editable=False),
                ),
                (
                    "changed_object_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "related_object_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="changes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-time"]},
        ),
        migrations.RemoveField(model_name="useraction", name="content_type"),
        migrations.RemoveField(model_name="useraction", name="user"),
        migrations.DeleteModel(name="UserAction"),
    ]
