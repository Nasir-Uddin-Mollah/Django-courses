# Generated by Django 5.1.5 on 2025-02-07 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelForm', '0002_mymodel_file_field_mymodel_float_field_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='generic_ip_address_field',
            field=models.GenericIPAddressField(default='none'),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='integer_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='json_field',
            field=models.JSONField(default='none'),
        ),
    ]
