from django.db import models
from products.models import Product,User
from django.db import models
from store.models import User

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.username


class Order(models.Model):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    person_address = models.CharField(max_length=100)
    person_landmark = models.CharField(max_length=100, blank=True)
    person_city = models.CharField(max_length=50)
    person_state = models.CharField(max_length=50)
    person_postalcode = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    # Add more fields as needed, such as payment status, delivery status, etc.

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} for {self.product.name} (Status: {self.status})"