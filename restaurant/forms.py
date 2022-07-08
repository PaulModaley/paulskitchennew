from django import forms
from django.conf import settings
from .models import Contact, Booking, UserProfile


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class NumberInput(forms.NumberInput):
    input_type = "number"


class TextInput(forms.TextInput):
    input_type = "text"


class EmailInput(forms.EmailInput):
    input_type = "email"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "message",
        ]
        widgets = {
            "name": TextInput(attrs={"class": "form-control"}),
            "email": EmailInput(attrs={"class": "form-control"}),
            "message": TextInput(attrs={"class": "form-control"}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "date",
            "time",
            "guests",
        ]
        widgets = {
            "date": DateInput(attrs={"class": "form-control"}),
            "time": forms.Select(attrs={"class": "form-control"}),
            "guests": forms.Select(attrs={"class": "form-control"}),
        }


class UserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "firstname",
            "lastname",
            "email",
        ]
        widgets = {
            "firstname": TextInput(attrs={"class": "form-control"}),
            "lastname": EmailInput(attrs={"class": "form-control"}),
            "email": TextInput(attrs={"class": "form-control"}),
        }
