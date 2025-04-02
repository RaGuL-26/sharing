from django.shortcuts import render,redirect
from .forms import registerform,loginform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def main_page(request):
    return render(request,'index.html')

def register_page(request):
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            form.save()
            print(user.password)
            messages.success(request,"Registered SuccessFully..!")
            return redirect('/')
    else:
            form = registerform()
    return render(request,'register.html',{'form':form})

from django.contrib.auth import authenticate, login

def login_page(request):
    if request.method == 'POST':
        form = loginform(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('/')
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = loginform()
    return render(request, 'login.html', {'form': form})

def logout_page(request):
    logout(request)
    messages.success(request,'LoggedOut SuccessFully..!')
    return redirect('/')
