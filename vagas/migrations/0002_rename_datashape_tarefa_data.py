# Generated by Django 4.1.3 on 2022-11-15 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vagas", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tarefa", old_name="datashape", new_name="data",
        ),
    ]
