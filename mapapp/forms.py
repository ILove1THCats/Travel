from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Location

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'latitude', 'longitude', 'description', 'category']