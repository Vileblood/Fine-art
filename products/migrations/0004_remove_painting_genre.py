# Generated by Django 3.1 on 2020-08-15 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200814_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='painting',
            name='genre',
        ),
    ]
