from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateStoreForm,ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product,Review,CartItem
from store import models as StoreModels

from django.db.models import Q


@login_required(login_url='loginpage')
def add_store(request):
    if request.method == 'POST':
        form = CreateStoreForm(request.POST,request.FILES)
        print('ejfnei')
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.owner = request.user
            new_product.save()
            
            file_path = new_product.image_of_product.path
            print("Uploaded image saved at:", file_path)
            messages.success(request,"Registered SuccessFully..!")
            return redirect('storepage')
        else:
            print(form.errors)
    else:
        print('jnfgvuner')
        form = CreateStoreForm()    
    return render(request,'addstore.html',{'form':form})



def store_page(request):
    query = request.GET.get('q')
    if query and query != 'all':
        store_details = Product.objects.filter(Q(product_type__icontains=query))
    else:
        store_details = Product.objects.all()
    return render(request,'stores.html',{'store_details':store_details})

@login_required(login_url='loginpage')
def product_page(request,slug):
    product_detail = Product.objects.get(slug=slug)
    product = get_object_or_404(Product,slug=slug)
    reviews = Review.objects.filter(product = product)
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('productpage',slug=slug)
    else:
        form = ReviewForm()
        
    return render(request,'product.html',{'product_detail':product_detail,'product':product,'reviews':reviews,'form':form})

@login_required(login_url='loginpage')
def add_to_cart(request,slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        try:
            quantity = int(quantity)
        except ValueError:
            quantity = 1 
            
        if quantity < 1:
            quantity = 1
        
        cart_item, created = CartItem.objects.get_or_create(
            product_of_user=product,
            particular_user=request.user,
            defaults={'quantity': quantity} 
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
    
    return redirect('productpage', slug=slug)

@login_required(login_url='loginpage')
def cart_page(request):
    cart_items = CartItem.objects.filter(particular_user =request.user)
    
    for cart_item in cart_items:
        cart_item.total_price = cart_item.quantity * cart_item.product_of_user.price
    
    return render(request,'cart.html',{'cart_items':cart_items})


@login_required(login_url='loginpage')
def delete_cart(request,id):
    cart_del = get_object_or_404(CartItem,id=id)
    if request.user == cart_del.particular_user:
        if request.method == 'POST':
            cart_del.delete()
            return redirect('cartpage')
    else:
        return redirect('cartpage')  
    return render(request,'cart.html',{'cart_del':cart_del})     

@login_required(login_url='loginpage')
def update_cart(request,id):
    cart_item = get_object_or_404(CartItem,id=id)
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity'))

        cart_item.quantity = new_quantity
        cart_item.save()
        return redirect('cartpage')
       
