# Generated by Django 3.1.5 on 2021-04-03 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_student_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_subjects',
            name='student_id',
            field=models.EmailField(max_length=254),
        ),
    ]
