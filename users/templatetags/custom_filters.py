#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import template


register = template.Library()


@register.filter
def addattrs(field, my_attrs):
    """
        Expand attributes of django forms' label input.
    """
    my_attrs = my_attrs.split(',')
    my_attrs = dict([attr.split('=') for attr in my_attrs])
    return field.as_widget(attrs=my_attrs)


@register.filter
def fieldtype(field):
    return field.field.widget.__class__.__name__
    # return field.field.widget.input_type
    # return dir(field.field.widget)
