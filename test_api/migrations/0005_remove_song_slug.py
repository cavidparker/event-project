# Generated by Django 3.1.3 on 2022-07-25 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0004_auto_20220725_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='slug',
        ),
    ]
