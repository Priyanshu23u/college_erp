# Generated by Django 4.2.13 on 2024-10-29 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dbms", "0003_alter_bookissued_book"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookissued",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dbms.libraryinventory"
            ),
        ),
    ]
