# Generated by Django 4.2.3 on 2023-09-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0003_num_people_remove_usertime_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertime',
            name='reserve_time',
            field=models.IntegerField(),
        ),
    ]