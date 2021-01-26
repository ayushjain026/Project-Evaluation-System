from django import forms
from .models import *


class HodForm(forms.ModelForm):
    class Meta:
        print("\n\n\n\n\nIn starting form")
        model = hod_registration
        fields = ["name",
            "password",
            "department",
            "college_url",
            "email",
            "phone_number",
            "id_card_image",
            "verification",
            "user_type"
            ]

        print("\n\n\n\n\nIn form")
