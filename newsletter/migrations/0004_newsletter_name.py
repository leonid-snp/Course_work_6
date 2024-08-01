# Generated by Django 5.0.7 on 2024-08-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0003_alter_newsletter_clients"),
    ]

    operations = [
        migrations.AddField(
            model_name="newsletter",
            name="name",
            field=models.CharField(
                default=None,
                help_text="Название рассылки",
                max_length=20,
                verbose_name="Название рассылки",
            ),
            preserve_default=False,
        ),
    ]
