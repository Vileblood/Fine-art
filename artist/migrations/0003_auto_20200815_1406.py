# Generated by Django 3.1 on 2020-08-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20200815_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='year',
        ),
        migrations.AddField(
            model_name='artist',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='death',
            field=models.DateField(blank=True, null=True),
        ),
    ]
