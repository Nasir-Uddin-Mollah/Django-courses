# Generated by Django 5.1.5 on 2025-02-07 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mymodel',
            fields=[
                ('auto_field', models.AutoField(primary_key=True, serialize=False)),
                ('big_integer_field', models.BigIntegerField()),
                ('binary_field', models.BinaryField()),
                ('boolean_field', models.BooleanField()),
                ('char_field', models.CharField(max_length=255)),
                ('decimal_field', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duration_field', models.DurationField(default=datetime.timedelta(days=1))),
            ],
        ),
    ]
