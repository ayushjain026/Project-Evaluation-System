# Generated by Django 3.1.5 on 2021-04-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_auto_20210403_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_histort',
            name='faculty_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
