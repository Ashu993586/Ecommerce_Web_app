# Generated by Django 2.0.6 on 2018-07-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0002_auto_20180710_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='update_at',
            field=models.TimeField(auto_now=True),
        ),
    ]
