#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import template

register = template.Library()


@register.inclusion_tag("snippets/form.html")
def form_extra(form, action, methods="POST"):
    """
    Expand style of django form and customize more attributs for django form,
    example for, <input ...>, we can attach some new attribut "placeholder" or
    "class" and etc.

    And the more disgin, look up the snippet "templates/snippets/form.html"
    """
    return {
        "form": form,
        "action": action,
        "methods": methods,
    }
