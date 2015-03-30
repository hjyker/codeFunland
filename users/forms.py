#!/usr/bin/env python
# encoding: utf-8


from django import forms
from django.forms.util import ErrorList, ValidationError
from django.contrib.auth.models import User

from users.models import UserProfile


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True
    )
    remember_me = forms.BooleanField(
        required=False
    )


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        label=u"密码"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        label=u"再次输入密码"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get("email", "")
        if not email:
            error_msg = u"email不能为空"
            raise ValidationError(error_msg)

        email_exist = User.objects.filter(email=email).exists()
        if email_exist:
            error_msg = u"email已存在"
            # self._errors["email"] = ErrorList([tips_msg])
            raise ValidationError(error_msg)
        return email

    def clean_password2(self):
        password = self.cleaned_data.get("password", "").strip()
        password2 = self.cleaned_data.get("password2", "").strip()

        if password and password2 and password != password2:
            error_msg = u"两次密码不一致"
            # self._errors['password'] = ErrorList([tips_msg])
            raise ValidationError(error_msg)
        return password2


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar_link']


class UploadFileForm(forms.Form):
    avatar = forms.ImageField()


class ImageFileForm(forms.Form):
    x1 = forms.CharField(widget=forms.HiddenInput(), initial=92)
    y1 = forms.CharField(widget=forms.HiddenInput(), initial=0)
    x2 = forms.CharField(widget=forms.HiddenInput(), initial=302)
    y2 = forms.CharField(widget=forms.HiddenInput(), initial=225)
    width = forms.CharField(widget=forms.HiddenInput(), initial=400)
    height = forms.CharField(widget=forms.HiddenInput(), initial=225)

