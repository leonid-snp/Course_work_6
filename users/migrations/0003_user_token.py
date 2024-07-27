# Generated by Django 5.0.7 on 2024-07-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="token",
            field=models.CharField(
                blank=True,
                help_text="Укажите токен",
                max_length=100,
                null=True,
                verbose_name="Токен",
            ),
        ),
    ]
