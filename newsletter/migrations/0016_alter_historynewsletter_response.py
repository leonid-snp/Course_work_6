# Generated by Django 5.0.7 on 2024-08-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0015_remove_historynewsletter_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historynewsletter",
            name="response",
            field=models.CharField(
                blank=True,
                help_text="Укажите ответ почтового сервиса",
                max_length=255,
                null=True,
                verbose_name="Ответ почтового сервиса",
            ),
        ),
    ]
