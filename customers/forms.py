from django import forms
from django.forms.widgets import ClearableFileInput
from django.contrib.auth import get_user_model
from .models import CustomUser


class ChangeProfileImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('profile_image',)
