from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views import View
from .cart import Cart
from product.models import Product
from .forms import CartAddForm, OofCodeForm
from .models import Address
# Create your views here.
from .models import Order, OrderItem, OofCode


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        form = OofCodeForm()
        return render(request, 'cart.html', {'cart': cart, 'form': form})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        if product:
            cart.add(product, int(request.POST['quantity']))
        return HttpResponse({'redirect': redirect('home:home').url})


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
        items = order.items.all()
        form = OofCodeForm()
        return redirect('orders:order_detail', order_id=order.id)


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
        return render(request, 'orders.html', {'orders': orders})


class OrderDetail(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id, is_deleted=False, checkout=False, user=request.user)
        items = order.items.all()
        form = OofCodeForm()
        address = Address.objects.get(user=request.user)
        return render(request, 'checkout.html', {"order": order, 'form': form, 'items': items, 'address': address})


class OrderRemoveView(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order.is_deleted = True
        order.save()
        return redirect('orders:orders')
