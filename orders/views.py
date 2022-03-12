from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart
from product.models import Product
from .forms import CartAddForm, OofCodeForm

# Create your views here.
from .models import Order, OrderItem, OofCode


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        form = OofCodeForm()
        return render(request, 'orders/cart.html', {'cart': cart, 'form': form})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
        return redirect('orders:cart')


class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('orders:cart')


class OrderCreate(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()

        return redirect('home:home')


class OofCodeApply(View):
    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        form = OofCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            code = OofCode.objects.get(code=code)
            order.set_discount(code.discount)
            order.save()
        return redirect('orders:order_detail', order_id=order_id)


class OrdersView(View):
    def get(self, request):
        orders = Order.objects.filter(user=request.user, is_deleted=False)
        return render(request, 'orders/orders.html', {'orders': orders})


class OrderDetail(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id, is_deleted=False)
        items = order.items.all()
        form = OofCodeForm()
        return render(request, 'orders/order_detail.html', {"order": order, 'form': form, 'items': items})


class OrderRemoveView(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order.is_deleted = True
        order.save()
        return redirect('orders:orders')
