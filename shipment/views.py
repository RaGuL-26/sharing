from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import AddressForm,OrderForm
from products.models import CartItem,Product
from .models import Address,Order
from django.db.models import F,Sum
from django.contrib.auth.decorators import login_required


@login_required(login_url='loginpage')
def buy_page(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.user.is_authenticated:
        user_addresses = Address.objects.filter(user=request.user)
        address_form = None
        
        print('User authenticated')
        print('User addresses:', user_addresses)
        
        if request.method == 'POST':
            print('POST request received')
            
            if 'address_id' in request.POST:
                address_id = request.POST.get('address_id')
                print('Address ID selected:', address_id)
            else:
                address_form = AddressForm(request.POST)
                if address_form.is_valid():
                    print('New address form is valid')
                    
                    address = address_form.save(commit=False)
                    address.user = request.user
                    address.save()
                    
                    messages.success(request, 'Address added successfully!')
                    return redirect('buypage', slug=slug)
                else:
                    print('New address form is invalid:', address_form.errors)
        else:
            address_form = AddressForm()
            print('Rendering page with address form:', address_form)
        
        return render(request, 'buy.html', {'user_addresses': user_addresses, 'address_form': address_form, 'product': product})
    else:
        print('User not authenticated')
        return render(request, 'buy.html', {'user_addresses': None, 'address_form': None, 'product': product})

@login_required(login_url='loginpage')
def confirm_msg(request, slug):
    print('confirm_msg view reached')
    address_id = request.POST.get('address_id')
    print('Address ID:', address_id)
    
    product = get_object_or_404(Product, slug=slug)

    person_address = get_object_or_404(Address, id=address_id).street_address
    person_landmark = get_object_or_404(Address, id=address_id).landmark
    person_city = get_object_or_404(Address, id=address_id).city
    person_state = get_object_or_404(Address, id=address_id).state
    person_postalcode = get_object_or_404(Address, id=address_id).postal_code
    
    # Filter cart items for the particular user and product
    cart_items = CartItem.objects.filter(particular_user=request.user)
    
    # Calculate total price for the product
    total_price = 0
    total_quantity = 0
    for cart_item in cart_items:
        if cart_item.product_of_user.name == product.name:
            total_price += cart_item.quantity * cart_item.product_of_user.price
            total_quantity += cart_item.quantity
    
    return render(request, 'confirmation.html', {
        'cart_items': cart_items,
        'product': product,
        'address_id': address_id,
        'person_address': person_address,
        'person_landmark': person_landmark,
        'person_city': person_city,
        'person_state': person_state,
        'person_postalcode': person_postalcode,
        'total_price': total_price,
        "total_quantity":total_quantity
    })


@login_required(login_url='loginpage')
def cancel_pay(request):
    messages.success(request,'Payment Aborted..!')
    return redirect('cartpage')


@login_required(login_url='loginpage')
def process_order(request, slug):
    if request.method == 'POST':
        form_data = request.POST.copy()
        form_data['user'] = request.user.pk 

        product = get_object_or_404(Product, slug=slug)
        form_data['product'] = product

        form = OrderForm(form_data)
        if form.is_valid():

            order = form.save()
            messages.success(request,"Ordered SuccessFully")
            return redirect('mainpage')
        else:
            print("Form is not valid")
            print("Form errors:", form.errors)
    else:
        pass

    return redirect('mainpage')


@login_required(login_url='loginpage')
def my_orders(request):
    my_order = Order.objects.filter(user = request.user).order_by('-created_at')   
        
    return render(request,'myorders.html',{'my_order':my_order})


@login_required(login_url='loginpage')
def seller_orders(request):
    seller_orders = Order.objects.filter(product__owner=request.user).order_by('-created_at')  
    return render(request, 'storeorders.html', {'seller_orders': seller_orders})


@login_required(login_url='loginpage')
def update_order_status(request):
    order_id = request.POST.get('order_id')
    new_status = request.POST.get('status')

    order = get_object_or_404(Order, id=order_id)
    
    if order.product.owner == request.user: 
        order.status = new_status
        order.save()
    
    return redirect('sellerorder')





