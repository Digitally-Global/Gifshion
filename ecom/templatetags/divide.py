from django import template
register = template.Library()

@register.filter
def divide(value,div):
    return round((float(value) / float(div)) , 2)

