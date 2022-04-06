from django.urls import path
from . import views, api

app_name = 'orders'

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', views.CartRemoveView.as_view(), name='cart_remove'),
    path('cart/checkout', views.OrderCreate.as_view(), name='create_order'),
    path('aplly/<int:order_id>/', views.OofCodeApply.as_view(), name="apply_code"),
    path('orders/', views.OrdersView.as_view(), name='orders'),
    path('order/detail/<int:order_id>', views.OrderDetail.as_view(), name='order_detail'),
    path('order/remove/<int:order_id>', views.OrderRemoveView.as_view(), name='order_remove'),
    path('orderitem/<int:pk>', api.OrderItemView.as_view(), name='order_item'),
]
