from django.shortcuts import render,get_list_or_404,redirect
from django.http import HttpResponse
from . models import Product
from .models import Cart
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    
    pro=Product.objects.all()
    return render(request,'facebook.html',{'pro':pro } )

@login_required
def add_to_cart(request,product_id):
    product =get_list_or_404(Product,id=product_id)
    cart_iteam, created=Cart.objects.get_or_create(user=request.user,product=product)
    if not created:
        cart_iteam.quantity +=1
        cart_iteam.save()
    return redirect('cart')
@login_required
def cart(request):
    cart_items=Cart.objects.filter(user=request.user)
    total= sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html',{'cart_items':cart_items, 'total':total})


