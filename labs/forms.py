#!/usr/bin/env python
# encoding: utf-8


from django import forms

from users.models import UserCode


class UserCodeForm(forms.Form):
    code_content = forms.CharField(
        widget=forms.Textarea())
