from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.Form):

    user_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    password1 = forms.CharField(
        label='password',
        max_length=32,
        min_length=8,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}
                                   ))

    password2 = forms.CharField(
        label='confirm password',
        max_length=32,
        min_length=8,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}
                                   ))

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        user = User.objects.filter(username=user_name).exists()

        if user:
            raise ValidationError('This username is already exists')

        return user_name

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()

        if user:
            raise ValidationError('This email address is already exists')

        return email

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')

        if p1 and p2 and p1 != p2:
            raise ValidationError('password must match')
