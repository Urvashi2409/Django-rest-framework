# Generated by Django 4.0.4 on 2023-07-15 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Movie',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='isDone',
            new_name='isActive',
        ),
    ]