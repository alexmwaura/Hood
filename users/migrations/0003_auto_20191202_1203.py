# Generated by Django 2.2.7 on 2019-12-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191202_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='location',
            name='estate',
            field=models.CharField(max_length=60),
        ),
    ]