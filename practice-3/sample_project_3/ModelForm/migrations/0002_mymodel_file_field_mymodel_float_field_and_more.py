# Generated by Django 5.1.5 on 2025-02-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelForm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='file_field',
            field=models.FileField(default=1, upload_to=''),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='float_field',
            field=models.FloatField(default=1.1),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='image_field',
            field=models.ImageField(default='myimage', upload_to=''),
        ),
    ]
