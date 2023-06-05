from django import template

register = template.Library()
@register.filter
def discount(price, Discount):
    if Discount == None or Discount == 0:
        return price
    
    sellprice = price
    sellprice = price - (price * Discount/100)
    return round(sellprice,2)