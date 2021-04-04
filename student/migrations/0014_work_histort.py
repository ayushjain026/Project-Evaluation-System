# Generated by Django 3.1.5 on 2021-04-02 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20210402_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='work_histort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=700)),
                ('student_id', models.IntegerField()),
                ('student_name', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=100)),
                ('semister', models.IntegerField()),
            ],
        ),
    ]
