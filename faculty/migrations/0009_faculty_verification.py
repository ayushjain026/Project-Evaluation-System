# Generated by Django 3.1.5 on 2021-03-28 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0008_auto_20210327_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='verification',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
