from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from allauth.account.forms import LoginForm, SignupForm, ChangePasswordForm
from django.core.exceptions import ValidationError
from allauth.utils import (
    get_request_param,
    get_user_model,
    import_callable,
    valid_email_or_none,
)

from django.contrib import messages

my_default_errors = {
    'required': 'این فیلد را پر کنید',
    'invalid': 'Enter a valid value'
}

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].error_messages = "fdkjj"
        self.fields['username'] = forms.CharField(label=':نام کاربری',
            widget=forms.TextInput(
                attrs={
                     "style" :"text-align:center; ",
                    "class" : " wrap-input100 main validate-input input100 ",
                    "id" : "username-signup",
                    "placeholder" : "نام کاربری را وارد کنید"
                    }
                )
        )
        self.fields['email'] = forms.CharField(label=': ایمیل',
                widget=forms.EmailInput(
                    attrs={
                        "style" :"text-align:center; ",
                        "class" : " wrap-input100 main validate-input input100 ",
                        "id" : "email-signup",
                        "placeholder" : "خود را وارد کنید  email "
                        }
                    )
        )
        self.fields['password1'] = forms.CharField(label=': کلمه عبور',
                widget=forms.PasswordInput(
                    attrs={
                        "style" :"text-align:center; ",
                        "class" : " wrap-input100 main validate-input input100 ",
                        "id" : "password1",
                        "placeholder" :" کلمه عبور را وارد کنید",
                     }
                ),

         )
        self.fields['password1'].error_messages  = {'required': 'custom required message'}

        self.fields['password2'] = forms.CharField(label=': تکرار کلمه عبور',
            widget=forms.PasswordInput(
                attrs={
                "style" :"text-align:center; ",
                "class" : " wrap-input100 main validate-input input100 ",
                "id" : "password2",
                "placeholder" :" کلمه عبور خود را تکرار کنید",
                }
            ), error_messages=my_default_errors
        )
        self.fields['password2'].widget.attrs.update({"error_messages":my_default_errors })


    def clean_password1(self):
        password1 = self.cleaned_data['password1']

        if ("password1" in self.cleaned_data and "password2" in self.cleaned_data):
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("رمز عبور و تکرار ان با هم تطابقت ندارد")
        return self.cleaned_data["password1"]


class CustomSignInForm(LoginForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CustomSignInForm, self).__init__(*args, **kwargs)
        self.fields['login'] = forms.CharField(label=': ایمیل',
            widget=forms.EmailInput(
                attrs={
                    "style" :"text-align:center; ",
                    "class" : " wrap-input100 main validate-input input100 ",
                    "id" : "email-signup",
                    "placeholder" : "خود را وارد کنید  email "
                }
            )
        )
        self.fields['password'] = forms.CharField(label=': کلمه عبور',
                widget=forms.PasswordInput(
                    attrs={
                        "style" :"text-align:center; ",
                        "class" : " wrap-input100 main validate-input input100 ",
                        "id" : "password1",
                        "placeholder" :" کلمه عبور را وارد کنید",
                     }
                ),
         )
        self.fields['remember'] = forms.BooleanField(label=': مرا به خاطر بسپار', initial=False, required=False )

class CustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CustomChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['oldpassword'] = forms.CharField(
                widget=forms.PasswordInput(
                    attrs={
                        "style" :"text-align:center; ",
                        "class" : " wrap-input100 main validate-input input100 ",
                        "id" : "password1",
                        "placeholder" :" کلمه عبور فعلی خود را وارد کنید",
                     }
                ),
         )
        self.fields['password1'] = forms.CharField(
             widget=forms.PasswordInput(
                 attrs={
                     "style" :"text-align:center; ",
                     "class" : " wrap-input100 main validate-input input100 ",
                     "id" : "password1",
                     "placeholder" :" رمز عبور جدید را وارد کنید",
                  }
             ),
        )
        self.fields['password2'] = forms.CharField(
              widget=forms.PasswordInput(
                  attrs={
                      "style" :"text-align:center; ",
                      "class" : " wrap-input100 main validate-input input100 ",
                      "id" : "password1",
                      "placeholder" :" رمز عبور جدید خود را تکرار کنید",
                   }
              ),
        )
