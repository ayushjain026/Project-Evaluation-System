from django.db import models


class hod_registration(models.Model):
    hod_fullname = models.CharField(max_length=30, default='abc')
    hod_username = models.CharField(max_length=30, default='abc')
    hod_password = models.CharField(max_length=50, default='abc')
    college_name = models.CharField(max_length=50, default='abc')
    college_department_name = models.CharField(max_length=100, default='abc')
    college_url = models.CharField(max_length=2048, default='abc')
    hod_email = models.EmailField(default='abc@gmail.com')
    hod_phone_number = models.CharField(max_length=12, default='123')
    hod_id_card_image = models.ImageField(upload_to='images/', default='')
    hod_verification = models.BooleanField()
    user_type = models.IntegerField()


class college_details(models.Model):
    college_name = models.CharField(max_length=100)
    college_url = models.CharField(max_length=2048)
    college_email = models.EmailField()
    college_phone_number = models.CharField(max_length=12)
    college_department_name = models.CharField(max_length=100)


class test(models.Model):
    image = models.ImageField(upload_to='images/')


