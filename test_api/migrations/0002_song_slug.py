# Generated by Django 3.1.3 on 2022-07-25 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(default=0, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
