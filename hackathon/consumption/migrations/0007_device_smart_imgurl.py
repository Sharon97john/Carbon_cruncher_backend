# Generated by Django 4.0.2 on 2022-10-23 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0006_consumption_calc_number_of_trees_treek'),
    ]

    operations = [
        migrations.AddField(
            model_name='device_smart',
            name='imgurl',
            field=models.CharField(default='/images/mini.png', max_length=100),
        ),
    ]