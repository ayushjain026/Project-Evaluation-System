# Generated by Django 3.1.5 on 2021-04-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20210331_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_title', models.CharField(max_length=250, null=True)),
                ('for_semister', models.IntegerField()),
                ('submission_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('submission_last_date', models.DateTimeField()),
                ('submission_file', models.FileField(upload_to='student_doc/')),
                ('submission_comment_student', models.CharField(default='none', max_length=2000, null=True)),
                ('faculty_email_auth', models.EmailField(max_length=254)),
                ('hod_email_auth', models.EmailField(max_length=254)),
                ('submission_department', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
