# Generated by Django 4.0.2 on 2022-10-23 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0004_rename_name_device_smart_user_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='consumption_calc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricty_consumption', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('family_members', models.IntegerField()),
                ('created_date', models.DateTimeField()),
                ('device_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='consumption.device_smart')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='consumption.user_table')),
            ],
        ),
    ]
