from django.db import models
from store.models import User

class Product(models.Model):
    ELECTRONICS = 'Electronics'
    CLOTHING = 'Clothing'
    BOOKS = 'Books'
    FURNITURE = 'Furniture'
    KITCHEN = 'Kitchen'
    BEAUTY = 'Beauty'
    SPORTS = 'Sports'
    TOYS = 'Toys'
    PHONES = 'Phones'
    COMPUTERS = 'Computers'
    OTHERS = 'others'

    PRODUCT_TYPES = [
        (ELECTRONICS, 'Electronics'),
        (CLOTHING, 'Clothing'),
        (BOOKS, 'Books'),
        (FURNITURE, 'Furniture'),
        (KITCHEN, 'Kitchen'),
        (BEAUTY, 'Beauty'),
        (SPORTS, 'Sports'),
        (TOYS, 'Toys'),
        (PHONES, 'Phones'),
        (COMPUTERS, 'Computers'),
        (OTHERS, 'others')
    ]


    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image_of_product = models.ImageField(upload_to='productImg',null=True)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    launch_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    ONESTAR = '⭐'
    TWOSTAR = '⭐⭐'
    THREESTAR = '⭐⭐⭐'
    FOURSTAR = '⭐⭐⭐⭐'
    FIVESTAR = '⭐⭐⭐⭐⭐'
    
    RATINGS_TYPES = [
        (ONESTAR, '⭐'),
        (TWOSTAR, '⭐⭐'),
        (THREESTAR, '⭐⭐⭐'),
        (FOURSTAR, '⭐⭐⭐⭐'),
        (FIVESTAR, '⭐⭐⭐⭐⭐'),
    ]
    
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    product_review = models.CharField(max_length=20, choices=RATINGS_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    
class CartItem(models.Model):
    product_of_user = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartitem')
    particular_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartitem')
    quantity = models.IntegerField()
    
    def __str__(self):
        return f'{self.particular_user.username}--{self.product_of_user.name}--quantity : {self.quantity}'