# Generated by Django 3.2.16 on 2023-02-01 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Required. 150 characters or fewer. ASCII letters and digits only.",
                verbose_name="staff status",
            ),
        ),
    ]
