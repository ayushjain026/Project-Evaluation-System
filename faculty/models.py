from django.db import models


class faculty(models.Model):
    fullname = models.CharField(max_length=50,null=True)
    username = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=60,null=True)
    college_name = models.CharField(max_length=50, default='abc',null=True)
    college_department_name = models.CharField(max_length=100, default='abc',null=True)
    faculty_email = models.EmailField(default='abc@gmail.com',null=True)
    subjects = models.CharField(max_length=50,null=True)
    user_type = models.IntegerField(null=True)


class temp_csv(models.Model):
    csv_file = models.FileField(upload_to='temp/documents/')
    department = models.CharField(max_length=60, null=True)
    hod_name = models.EmailField(default='abc@gmail.com')