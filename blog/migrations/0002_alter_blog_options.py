# Generated by Django 5.0.7 on 2024-08-11 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={
                "permissions": [("can_view_blog", "Can view blog")],
                "verbose_name": "Блог",
                "verbose_name_plural": "Блог",
            },
        ),
    ]