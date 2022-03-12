from rest_framework import generics
from .serializers import OrderItemSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .models import OrderItem, Order


class OrderItemView(generics.RetrieveAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        self.queryset = OrderItem.objects.filter(order_id=self.kwargs['pk'])
        return super().get_queryset()


class OrderView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
