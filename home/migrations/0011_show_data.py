# Generated by Django 3.2.9 on 2021-11-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20211120_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=100)),
                ('percent', models.CharField(max_length=100)),
                ('correct', models.CharField(max_length=100)),
                ('wrong', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
            ],
        ),
    ]
