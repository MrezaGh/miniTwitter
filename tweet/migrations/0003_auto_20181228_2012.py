# Generated by Django 2.1.3 on 2018-12-28 16:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_auto_20181228_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 28, 16, 42, 21, 443110, tzinfo=utc), verbose_name='date published'),
        ),
    ]
