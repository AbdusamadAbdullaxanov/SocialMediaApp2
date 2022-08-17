from django import forms
from .models import Posts


class SearchBarForm(forms.Form):
    search_field = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "type here...", "style": "width: 350px; height: 50px;"}
        )
    )


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ("user", "text")
        widgets = {
            "user": forms.TextInput(attrs={"class": "form-control", "placeholder": "your username..."}),
            "text": forms.Textarea(attrs={"class": "form-control", "placeholder": "Type anything you want..."}),
        }
