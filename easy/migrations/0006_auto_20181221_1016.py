# Generated by Django 2.1.4 on 2018-12-21 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy', '0005_auto_20181220_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='guests',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='guests',
            name='email',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='guests',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='guests',
            name='zip_code',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
