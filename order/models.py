from django.db import models
from payment.models import Pay
# from .cart.models import Cart
from django.db import models
from cart.models import Cart
from payment.models import Pay

from shipping.models import Shipping
from customer_management.models import Customer

   # Define your payment fields here

class Order(models.Model):
    payment = models.OneToOneField(Pay, on_delete=models.PROTECT, null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE, null=True)
    shipping = models.ForeignKey(Shipping,on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=32)
    quantity = models.PositiveBigIntegerField()
    total = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
