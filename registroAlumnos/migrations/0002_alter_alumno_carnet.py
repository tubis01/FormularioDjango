# Generated by Django 5.0.3 on 2024-03-05 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registroAlumnos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alumno",
            name="carnet",
            field=models.CharField(max_length=15, unique=True),
        ),
    ]