# Generated by Django 4.2.10 on 2024-03-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='foreign',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
