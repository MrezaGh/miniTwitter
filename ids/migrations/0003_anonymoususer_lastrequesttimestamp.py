# Generated by Django 2.1.3 on 2018-12-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ids', '0002_requestinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymoususer',
            name='lastRequestTimeStamp',
            field=models.IntegerField(default=1546098673.990084),
        ),
    ]
