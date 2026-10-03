from django import forms
from .models import AdoptionRequest


class AdoptionRequestForm(forms.ModelForm):

    class Meta:
        model = AdoptionRequest

        fields = [
            "phone",
            "address",
            "reason",
            "previous_pet_experience",
            "message",
        ]

        widgets = {
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Enter your phone number"
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "placeholder": "Enter your full address",
                    "rows": 4
                }
            ),

            "reason": forms.Textarea(
                attrs={
                    "placeholder": "Why do you want to adopt this pet?",
                    "rows": 4
                }
            ),

            "previous_pet_experience": forms.CheckboxInput(),

            "message": forms.Textarea(
                attrs={
                    "placeholder": "Any additional message (optional)",
                    "rows": 4
                }
            ),
        }

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()

        if len(phone) < 8:
            raise forms.ValidationError(
                "Please enter a valid phone number."
            )

        return phone

    def clean_address(self):
        address = self.cleaned_data["address"].strip()

        if len(address) < 5:
            raise forms.ValidationError(
                "Please enter a valid address."
            )

        return address

    def clean_reason(self):
        reason = self.cleaned_data["reason"].strip()

        if len(reason) < 10:
            raise forms.ValidationError(
                "Please provide a little more detail about your reason."
            )

        return reason