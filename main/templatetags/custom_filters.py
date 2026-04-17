from django import template

register = template.Library()

@register.filter
def prettify_symptom(value):
    return value.replace('_', ' ').title()