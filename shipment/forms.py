from django import forms
from .models import Address,Order
from store.models import User
from products.models import Product

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_address','landmark','city', 'state', 'postal_code']
        
class OrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput())
    
    class Meta:
        model = Order
        fields = ['user', 'product', 'quantity', 'total_price', 'person_address', 'person_landmark', 'person_city', 'person_state', 'person_postalcode']

