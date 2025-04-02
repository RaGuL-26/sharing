from products.models import Product,Review,CartItem
from django import forms 

class CreateStoreForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','brand','image_of_product','description','product_type','color','price','slug']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'product_review']
        labels = {
            'text': 'Review',
            'product_review':'Stars'
        }
