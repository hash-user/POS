# Generated by Django 4.2.10 on 2024-03-17 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_pos_information_connection_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='new_pos_request',
            new_name='pos_request',
        ),
    ]