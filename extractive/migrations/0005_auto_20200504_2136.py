# Generated by Django 3.0.4 on 2020-05-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extractive', '0004_auto_20200503_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(),
        ),
    ]
