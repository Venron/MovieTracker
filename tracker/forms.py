from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput, PasswordInput, DateTimeInput, NumberInput
from .models import Track

style = 'border-color: black; border-width: 3px; font-weight: bold; font-size: medium; padding-left: 7px;'
width = 'col-sm-5'


class UserForm(forms.ModelForm):
    # style = 'border-color: black; border-width: 3px; font-weight: bold; font-size: medium; padding-left: 7px;'
    # width = 'col-sm-5'

    email = forms.CharField(widget=TextInput(attrs={'style': style, 'class': width}))
    username = forms.CharField(widget=TextInput(attrs={'style': style, 'class': width}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'style': style, 'class': width}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'style': style, 'class': width}))
    first_name = forms.CharField(max_length=100, widget=TextInput(attrs={'style': style, 'class': width}))
    last_name = forms.CharField(max_length=100, widget=TextInput(attrs={'style': style, 'class': width}))

    class Meta:
        model = User
        fields = ["email", "username", "password", "confirm_password", "first_name", "last_name"]

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password and confirmed password did not match")


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=TextInput(attrs={'style': style, 'class': width}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'style': style, 'class': width}))


class TrackForm(forms.ModelForm):
    # season = forms.IntegerField(widget=NumberInput(attrs={'style': style, 'class': width}))
    # started = forms.DateTimeField(widget=DateTimeInput(auto_now_add=True, attrs={'style': style, 'class': width}))
    # title = forms.CharField(widget=TextInput(attrs={'style': style, 'class': width}))

    title = models.CharField()
    season = models.PositiveIntegerField()
    episode = models.PositiveIntegerField()
    started = models.DateTimeField()

    class Meta:
        model = Track
        fields = ["title", "season", "episode"]
        widgets = {
            'title' : TextInput(attrs={'style': style, 'class': width}),
            'season' : NumberInput(attrs={'style': style, 'class': width}),
            'episode' : NumberInput(attrs={'style': style, 'class': width}),
        }
