from django.db import models


class hod_registration(models.Model):
    fullname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    college_name = models.CharField(max_length=50)
    department = models.CharField(max_length=30)
    college_url = models.CharField(max_length=2048)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    id_card_image = models.ImageField(upload_to="system/image", default="")
    verification = models.BooleanField()
    user_type = models.IntegerField()





