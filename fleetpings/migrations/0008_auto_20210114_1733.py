# Generated by Django 3.1.5 on 2021-01-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fleetpings", "0007_mysql8_default_value_fixes_20201003_1232"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webhook",
            name="url",
            field=models.CharField(
                help_text=(
                    "URL of this webhook, e.g. "
                    "https://discord.com/api/webhooks/123456/abcdef or "
                    "https://hooks.slack.com/services/xxxx/xxxx"
                ),
                max_length=255,
                unique=True,
            ),
        ),
    ]