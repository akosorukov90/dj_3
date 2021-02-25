from django import template

register = template.Library()


@register.filter()
def str_to_float(value):
    result = float(value)
    return result
