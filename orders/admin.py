from django.contrib import admin
from .models import Order, OrderItem, OofCode


# Register your models here.

class OrderItemLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'paid')
    list_filter = ('paid',)
    inlines = (OrderItemLine,)


@admin.register(OofCode)
class OofCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'valid_from', 'valid_to', 'discount', 'is_active')
    list_filter = ('is_active', 'valid_from', "valid_to")
