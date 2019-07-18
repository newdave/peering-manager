# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 00:58


from django.db import migrations, models
import peering.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Network",
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
                ("asn", peering.fields.ASNField(unique=True)),
                ("name", models.CharField(max_length=255)),
                ("irr_as_set", models.CharField(blank=True, max_length=255, null=True)),
                ("info_prefixes6", models.PositiveIntegerField(blank=True, null=True)),
                ("info_prefixes4", models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Synchronization",
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
                ("time", models.DateTimeField()),
                ("number_of_objects", models.PositiveIntegerField()),
            ],
        ),
    ]
