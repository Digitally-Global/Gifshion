from django import template
from ecom.models import Product_Stock
register = template.Library()

@register.filter
def divide(value,div):
    return round(float(value) / float(div) , 2)

@register.filter()
def multiply(value, arg):
    return round(float(value) * arg,2)

@register.filter()
def sub(value, arg):
    return round(float(value) - arg,2)\

def get_inStock(dataset):
    inStock = []
    for data in dataset:
        if int(data.stock) > 0:
            inStock.append(data)
        else:
            if data.product_stock_set.all().exists():
                for stock in data.product_stock_set.all():
                    if int(stock.stock) > 0:
                        inStock.append(data)
                        break
    return inStock

def displ(data):
    if int(data.stock) > 0:
        return True
    else:
        if data.product_stock_set.all().exists():
            for stock in data.product_stock_set.all():
                if int(stock.stock) > 0:
                    return True
    return False
@register.filter()
def filter_stock(value):
    return get_inStock(value)

@register.filter()
def display_none(value):
    return displ(value) 

@register.filter()
def check_corr(cart_item):
    for item in cart_item:
        print('Hello',item.size,item.color)
        if item.size and item.color: 
            for stock in item.product.product_stock_set.all():
                if stock.Color == item.color and stock.Size == item.size:
                    _stock = Product_Stock.objects.get(Size = item.size,Color=item.color,Product=item.product)
                    if _stock.stock >= item.quantity:
                        pass
                    else:
                        return True
        elif item.size:
            for stock in item.product.product_stock_set.all():
                if stock.Size == item.size:
                    _stock = Product_Stock.objects.get(Size = item.size,Color=None,Product=item.product)
                    if _stock.stock >= item.quantity:
                        print(_stock.stock,item.quantity)
                        pass
                    else:
                        return True
        elif item.color:
            for stock in item.product.product_stock_set.all():
                print('Stock',stock)
                if stock.Color == item.color:
                    _stock = Product_Stock.objects.get(Size = None,Color=item.color ,Product=item.product)
                    if _stock.stock >= item.quantity:
                        pass
                    else:
                        return True
        else:
            if item.product.stock >= item.quantity:
                pass
            else:
                return True
            
@register.filter()
def unavailable(item):
    if item.size and item.color: 
        for stock in item.product.product_stock_set.all():
            if stock.Color == item.color and stock.Size == item.size:
                _stock = Product_Stock.objects.get(Size = item.size,Color=item.color,Product=item.product)
                if _stock.stock >= item.quantity:
                    pass
                else:
                    return True
    elif item.size:
        for stock in item.product.product_stock_set.all():
            if stock.Size == item.size:
                _stock = Product_Stock.objects.get(Size = item.size,Color=None,Product=item.product)
                if _stock.stock >= item.quantity:
                    print(_stock.stock,item.quantity)
                    pass
                else:
                    return True
    elif item.color:
        for stock in item.product.product_stock_set.all():
            print('Stock',stock)
            if stock.Color == item.color:
                _stock = Product_Stock.objects.get(Size = None,Color=item.color ,Product=item.product)
                if _stock.stock >= item.quantity:
                    pass
                else:
                    return True
    else:
        if item.product.stock >= item.quantity:
            pass
        else:
            return True
    
    
@register.filter()
def mail(value):
    email = value.split('@')[0]
    provider = value.split('@')[1]
    email = email[0:2] + '*' * (len(email) - 2)
    return email + '@' + provider


@register.filter()
def get_15(value):
    return value.order_by('-id')[:15]
    