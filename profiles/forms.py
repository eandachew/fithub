from django import forms
from .models import UserProfile, Delivery  # Add Delivery import


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["bio", "profile_image"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = [
            "full_name",
            "email",
            "phone_number",
            "address_line1",
            "address_line2",
            "city",
            "postal_code",
            "country",
        ]
        widgets = {
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Full name for delivery"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "your@email.com"}
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone number for delivery updates",
                }
            ),
            "address_line1": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Street address"}
            ),
            "address_line2": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Apartment, suite, unit (optional)",
                }
            ),
            "city": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "City"}
            ),
            "postal_code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Postal code"}
            ),
            "country": forms.Select(
                attrs={"class": "form-control"},
                choices=[
                    ("", "Select country"),
                    ("Ireland", "Ireland"),
                    ("United Kingdom", "United Kingdom"),
                    ("United States", "United States"),
                    ("Germany", "Germany"),
                    ("France", "France"),
                    ("Spain", "Spain"),
                    ("Italy", "Italy"),
                ],
            ),
        }
