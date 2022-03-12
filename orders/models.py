from django.db import models
from core.models import BaseModel
# Create your models here.
from customer.models import User
from product.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator


class Order(BaseModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)
    discount = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f"{self.user} - {self.id}"

    def set_discount(self, value):
        self.discount = value

    @property
    def get_total_price(self):
        total = sum(item.get_cost for item in self.items.all())
        if self.discount:
            return total - total * int(self.discount) / 100
        return total


class OrderItem(BaseModel):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='order_item')
    price = models.IntegerField()
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.id)

    @property
    def get_cost(self):
        return self.quantity * self.price


class OofCode(BaseModel):
    code = models.CharField(max_length=30, unique=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.code
