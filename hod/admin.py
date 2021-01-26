from django.contrib import admin
from . models import hod_registration

# Register your models here.


class hod_admin(admin.ModelAdmin):
    list_display = [
        "name",
        "password",
        "department",
        "college_url",
        "email",
        "phone_number",
        "id_card_image",
        "verification",
        "user_type" ]


admin.site.register(hod_registration, hod_admin)
