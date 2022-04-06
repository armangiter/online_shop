from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}


def user(request):
    return {'user': request.user}
