from django import template
register = template.Library()

@register.filter
def divide(value,div):
    return round(float(value) / float(div) , 2)

@register.filter()
def multiply(value, arg):
    return round(float(value) * arg,2)

@register.filter()
def sub(value, arg):
    return round(float(value) - arg,2)