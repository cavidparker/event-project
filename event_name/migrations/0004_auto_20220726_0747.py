# Generated by Django 3.1.3 on 2022-07-26 07:47

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_name', '0003_auto_20220725_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventcard',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
