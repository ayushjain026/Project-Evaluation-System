# Generated by Django 3.1.5 on 2021-03-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0010_auto_20210328_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='college_department_name',
        ),
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(default='abc', max_length=100, null=True),
        ),
    ]
