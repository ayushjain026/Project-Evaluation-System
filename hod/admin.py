from django.contrib import admin
from . models import *

# Register your models here.


class hod_admin(admin.ModelAdmin):
    list_display = [
        'hod_fullname',
        'hod_username',
        'hod_password',
        'college_name',
        'department',
        'college_url',
        'hod_email',
        'hod_phone_number',
        'hod_id_card_image',
        'hod_verification',
        'user_type',
         ]


admin.site.register(hod_registration)
admin.site.register(college_details)
