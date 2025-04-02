from .models import User
from django import forms

class registerform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = User
        fields = ['email','username','password','dob','user_type']
        
        
class loginform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','password']
        

