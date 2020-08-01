from django import template

register = template.Library()


@register.filter
def replace_spaces(string):
    return string.replace(' ', '_')
