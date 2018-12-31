# Generated by Django 2.1.4 on 2018-12-31 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ids', '0003_anonymoususer_lastrequesttimestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogInTable',
            fields=[
                ('myip', models.IntegerField(primary_key=True, serialize=False)),
                ('mysession', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='anonymoususer',
            name='lastRequestTimeStamp',
            field=models.IntegerField(default=1546253139.076805),
        ),
    ]