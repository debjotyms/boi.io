from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .carts import Cart
from accounts.models import Book

class AddToCart(generic.View):
    def post(self, *args, **kwargs):
        product = get_object_or_404(Book, id=self.kwargs['product_id'])
        cart = Cart(self.request)
        cart.update(product.id, 1)
        return redirect('books')


class CartItems(generic.TemplateView):
    template_name = 'pages/cart.html'

    def get(self, request, *args, **kwargs):
        product_id = request.GET.get('product_id', None)
        quantity = request.GET.get('quantity', None)
        clear = request.GET.get('clear', False)

        if product_id and quantity:
            cart = Cart(request)
            cart.update(int(product_id), int(quantity))
            return redirect('cart')
        
        if clear:
            cart = Cart(request)
            cart.clear()
            return redirect('cart')
            
        return super().get(request, *args, **kwargs)