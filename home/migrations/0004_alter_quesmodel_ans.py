# Generated by Django 3.2.9 on 2021-11-20 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_quesmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quesmodel',
            name='ans',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
