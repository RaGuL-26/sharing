"""
URL configuration for digitalden project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views as StoreViews
from products import views as ProductViews
from shipment import views as Shipviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',StoreViews.main_page,name='mainpage'),
    path('register',StoreViews.register_page,name='registerpage'),
    path('login',StoreViews.login_page,name='loginpage'),
    path('logout',StoreViews.logout_page,name='logout'),
    path('addstore',ProductViews.add_store,name='addstore'),
    path('storepage',ProductViews.store_page,name='storepage'),
    path('product/<slug:slug>',ProductViews.product_page,name='productpage'),
    path('add_to_cart/<slug:slug>/', ProductViews.add_to_cart, name='addtocart'),
    path('cartpage', ProductViews.cart_page, name='cartpage'),
    path('deletecart/<int:id>',ProductViews.delete_cart,name='deletecart'),
    path('update_cart/<int:id>/', ProductViews.update_cart, name='updatecart'),
    path('<slug:slug>/buypage',Shipviews.buy_page,name='buypage'),
    path('<slug:slug>/confirmpage',Shipviews.confirm_msg,name='confirmpage'),
    path('cancelpay',Shipviews.cancel_pay,name='cancelpay'),
    path('<slug:slug>/processpurchase',Shipviews.process_order,name='processpurchase'),
    path('myorders',Shipviews.my_orders,name='myorders'),
    path('sellerorder',Shipviews.seller_orders,name='sellerorder'),
    path('updatestatus',Shipviews.update_order_status,name='updatestatus')
    

]


if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
