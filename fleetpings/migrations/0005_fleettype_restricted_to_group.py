# Generated by Django 2.2.16 on 2020-09-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
        ("fleetpings", "0004_auto_20200915_1617"),
    ]

    operations = [
        migrations.AddField(
            model_name="fleettype",
            name="restricted_to_group",
            field=models.ManyToManyField(
                blank=True,
                help_text="Restrict this fleet type to the following group(s) ...",
                related_name="fleettype_require_groups",
                to="auth.Group",
            ),
        ),
    ]
