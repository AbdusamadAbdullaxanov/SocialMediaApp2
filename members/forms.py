from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password"
        )

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "your username..."}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "your firstname..."}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "your lastname..."}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "email..."}),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "create strong password..."}
            ),
        }


class LoginUserForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=False,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control", "placeholder": "username",
                "style": 'width:400px; height:40px; margin: 1px auto;'
            }
        )
    )

    password = forms.CharField(
        label="Password",
        required=False,
        max_length=12,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", "placeholder": "password",
                "style": "width:400px; height:40px; margin: 1px auto;"
            }
        )
    )


class EmailForm(forms.Form):
    subject = forms.CharField(
        required=False,
        label="subject",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter title..."}
        )
    )

    email = forms.CharField(
        required=False,
        label="Email",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "type here..."}
        )
    )

    sender = forms.EmailField(
        required=False,
        label="Sender",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "type here..."}
        )
    )
