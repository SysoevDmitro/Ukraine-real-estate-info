from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Realtor


class HouseSearchForm(forms.Form):
    model = forms.CharField(max_length=255,
                            required=False,
                            label="",
                            widget=forms.TextInput(
                                attrs={"placeholder": "Search by "}))


class RealtorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Realtor
        fields = UserCreationForm.Meta.fields + (
            "rating",
            "first_name",
            "last_name",
        )


class RealtorUpdateForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = ["rating"]


class RealtorUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}))


class HouseSearchForm(forms.Form):
    price = forms.CharField(max_length=255,
                            required=False,
                            label="",
                            widget=forms.TextInput(
                                attrs={"placeholder": "Search by price"}))
