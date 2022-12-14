# Generated by Django 4.1.1 on 2022-09-22 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importance', models.IntegerField()),
                ('time', models.TimeField(default=datetime.time(14, 7, 43, 961758))),
                ('message', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Telegram UserID'),
        ),
    ]
