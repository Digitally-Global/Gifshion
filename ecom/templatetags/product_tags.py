from django import template


register = template.Library()


@register.inclusion_tag(filename='navbar.html', takes_context=True)
def navbar_context(context):
    return {
        'product_tags': context['product_tags'],
    }

    
