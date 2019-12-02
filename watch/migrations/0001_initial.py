# Generated by Django 2.2.7 on 2019-12-02 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=60)),
                ('station_details', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='media/images')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['station_name'],
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=60)),
                ('hospital_details', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='media/images')),
                ('location', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='users.Location')),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['hospital_name'],
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='media/images')),
                ('date_posted', models.DateField(auto_now=True)),
                ('details', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]