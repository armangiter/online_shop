from rest_framework import generics
from .serializers import OrderItemSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .models import OrderItem, Order


class OrderItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem





