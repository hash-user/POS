# Generated by Django 4.2.10 on 2024-03-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_pos_information_sim_network_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pos_information',
            name='connection_type',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
