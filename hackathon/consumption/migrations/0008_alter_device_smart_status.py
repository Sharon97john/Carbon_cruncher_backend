# Generated by Django 4.0.2 on 2022-10-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0007_device_smart_imgurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device_smart',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
