# Generated by Django 3.1.5 on 2021-03-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_auto_20210321_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='college_department_name',
            field=models.CharField(default='abc', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='college_name',
            field=models.CharField(default='abc', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='faculty_email',
            field=models.EmailField(default='abc@gmail.com', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='password',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
