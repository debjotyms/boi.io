from django.conf import settings

from accounts.models import Book


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        self.cart_id = settings.CART_ID
        cart = self.session.get(self.cart_id)
        self.cart = self.session[self.cart_id] = cart if cart else {}
    
    def update(self, product_id, quantity=1):
        product = Book.objects.get(id=product_id)
        self.session[self.cart_id].setdefault(str(product_id), {"quantity":0})
        update_quantity = self.session[self.cart_id][str(product_id)]['quantity'] + quantity
        self.session[self.cart_id][str(product_id)]['quantity'] = update_quantity
        self.session[self.cart_id][str(product_id)]['subtotal'] = update_quantity * float(product.price)

        if update_quantity < 1:
            del self.session[self.cart_id][str(product_id)]

        self.save()
    
    def __iter__(self):
        book_ids = self.cart.keys()
        pro = Book.objects.filter(id__in=(book_ids))
        cart = self.cart.copy()

        for item in pro:
            product = Book.objects.get(id=item.id)
            cart[str(item.id)]['product'] = {
                'id': item.id,
                'title': item.title,
                'price': float(item.price),
                'quantity': cart[str(item.id)]['quantity'],
            }
            yield cart[str(item.id)]

    
    def save(self):
        self.session.modified = True

    def __len__(self):
        return len(list(self.cart.keys()))

    def clear(self):
        try:
            del self.session[self.cart_id]
        except:
            pass
        self.save()