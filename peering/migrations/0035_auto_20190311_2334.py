# Generated by Django 2.1.7 on 2019-03-11 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("peering", "0034_auto_20190308_1954")]

    operations = [
        migrations.AlterField(
            model_name="routingpolicy",
            name="type",
            field=models.CharField(
                choices=[
                    ("export-policy", "Export"),
                    ("import-policy", "Import"),
                    ("import-export-policy", "Import and Export"),
                ],
                default="import-policy",
                max_length=50,
            ),
        )
    ]
