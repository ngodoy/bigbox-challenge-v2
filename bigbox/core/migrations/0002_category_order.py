# Generated by Django 3.2.1 on 2021-10-22 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="order",
            field=models.IntegerField(default=0, verbose_name="orden"),
        ),
    ]