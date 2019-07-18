# Generated by Django 2.1.7 on 2019-03-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("peering", "0033_router_encrypt_passwords")]

    operations = [
        migrations.AlterModelOptions(
            name="routingpolicy",
            options={
                "ordering": ["-weight", "name"],
                "verbose_name_plural": "routing policies",
            },
        ),
        migrations.AddField(
            model_name="routingpolicy",
            name="weight",
            field=models.PositiveSmallIntegerField(
                default=0, help_text="The higher the number, the higher the priority"
            ),
        ),
    ]
