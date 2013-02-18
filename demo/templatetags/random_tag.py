from django import template
from random import randint

register = template.Library()

@register.filter
def random_header(values):
    a, b = values.split()
    return randint(int(a), int(b))
