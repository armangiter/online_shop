from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password Confirm'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone', 'full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError(_('password not match'))
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text=_('you can change password using <a href=\"../password/\">this form<a>'))

    class Meta:
        model = User
        fields = ('email', 'phone', 'full_name', 'password', 'last_login')


class UserRegistrationsFrom(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(label='full name')
    phone = forms.CharField(max_length=13)
    password = forms.CharField(widget=forms.PasswordInput)
