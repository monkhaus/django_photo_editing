# Generated by Django 3.0.8 on 2020-08-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0002_auto_20200804_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
