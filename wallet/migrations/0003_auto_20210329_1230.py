# Generated by Django 3.1.7 on 2021-03-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_auto_20210329_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_id',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
