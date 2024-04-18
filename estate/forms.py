from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class HouseSearchForm(forms.Form):
    model = forms.CharField(max_length=255,
                            required=False,
                            label="",
                            widget=forms.TextInput(
                                attrs={"placeholder": "Search by "}))
