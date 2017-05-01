from django.conf import settings

from django import template

register = template.Library()


@register.simple_tag
def get_setting(name, default=None):
    """Returns the value of django settings given as name"""
    return getattr(settings, name, default)
