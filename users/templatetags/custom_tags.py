#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import template

from users.forms import (UserLoginForm, UserRegisterForm)


register = template.Library()


@register.inclusion_tag("snippets/form.html")
def form_extra(form, action, submit_value, methods="POST"):
    """
    Expand style of django form and customize more attributs for django form,
    example for, <input ...>, we can attach some new attribut "placeholder" or
    "class" and etc.

    And the more disgin, look up the snippet "templates/snippets/form.html"
    """

    return {
        "form": form,
        "action": action,
        "submit_value": submit_value,
        "methods": methods,
    }


@register.inclusion_tag("snippets/dialog_form.html")
def dialog_form(methods="POST"):
    """
    It's a dialog that combine Login form and Register form.
    """

    register_form = UserRegisterForm()
    login_form = UserLoginForm()
    register_action = "users:user_register"
    login_action = "users:user_login"

    return {
        "register_form": register_form,
        "login_form": login_form,
        "login_action": login_action,
        "register_action": register_action,
        "methods": methods
    }
