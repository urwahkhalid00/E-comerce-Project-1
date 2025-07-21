from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Product, Category, Brand, Cart, Order
from .forms.user_create_form import UserCreateForm
from .forms.contact_form import ContactForm
from .forms.checkout_form import CheckoutForm
from django.contrib import messages

from django.contrib.auth import authenticate, login,logout

def home(request):
    return render(request,'home.html')

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    return render(request, 'product_list.html', {'products': products, 'categories': categories, 'brands': brands})

def product_detail(request, id): 
    product = Product.objects.get(id=id)    
    return render(request, 'product_detail.html', {'product': product})



# def category_list(request):
#     categories = Category.objects.all()
#     return render(request, 'category_list.html', {'categories': categories})



def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'brand_list.html', {'brands': brands})

# def cart(request):
#     return render(request,'cart.html')


def cart(request):
     total = 0
     user_id = request.user.id
     shipping_charges = 150.00
     cart_items = Cart.objects.filter(user = user_id)
     for item in cart_items:
        total = total + item.sub_total
    
     tax = float(total) * 0.04
    # return HttpResponse( tax )
    
     grand_total = float(total) + tax + shipping_charges
    # return HttpResponse(user_id)

     return render(request,'cart.html', { 
        'cart_items': cart_items, 
        'total' :total, 
        'shipping_charges' : shipping_charges,
        'tax' : tax,
        'grand_total' :grand_total } )

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        qty = request.POST['quantity']
        
        product = Product.objects.get(pk=product_id)
        user_id = request.user.id
        
        try:
            cart_item = Cart.objects.get(product = product, user = user_id)
            cart_item.qty = cart_item.qty + int(qty)
            cart_item.sub_total =  cart_item.qty * product.price
            cart_item.save()
        except Cart.DoesNotExist:
            sub_total = product.price * int(qty)
            cart = Cart(product=product, qty=qty, sub_total = sub_total, user = user_id)
            cart.save()
            return redirect('cart')
    else:
        return redirect('product_list')
    # return HttpResponse(check_cart)   

    return redirect('cart')
    # return HttpResponse(request)
        
def delete_cart_item(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    if cart_item.user == request.user.id:
        cart_item.delete()
    return redirect('cart')     


def checkout(request):
    total = 0
    user_id = request.user.id
    shipping_charges = 150.00
    cart_items = Cart.objects.filter(user = user_id)
    for item in cart_items:
        total = total + item.sub_total
    
    tax = float(total) * 0.04
    # return HttpResponse( tax )
    
    grand_total = float(total) + tax + shipping_charges
    # return HttpResponse(user_id)


    if request.method == 'GET':
        checkout_form = CheckoutForm()
        # return HttpResponse(checkout_form)

        return render(request,'checkout.html',{ 
        'cart_items': cart_items, 
        'total' :total, 
        'shipping_charges' : shipping_charges,
        'tax' : tax,
        'grand_total' :grand_total,
        'form' : checkout_form  })
    else:
        # return HttpResponse( request.user.email )
        form = CheckoutForm(request.POST )
        form.user =  request.user
        if form.is_valid():
            # return HttpResponse(form)
            
            form.order_price = grand_total
            order = form.save()
            
            order.user.set = request.user
            
            order.order_price = grand_total
            order.save()

        
        else:
            return HttpResponse(form.errors)
            return HttpResponse('invalid data.')
        # return HttpResponse(request.POST)
        return redirect('product_list')

def my_account(request):
    return render(request,'my-account.html')

def wishlist(request):
    return render(request,'wishlist.html')

def register(request):
    if request.method == 'POST':
        # return HttpResponse(request.POST)
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('user created successfully!')
            return redirect('login')
        else:
            return HttpResponse(form.errors )
            return HttpResponse('please provide authentic data')
    else:
        # form = UserCreateForm()  # Create an empty form instance
        return HttpResponse('Method not Allowed!.')
        # return render(request, 'signup.html', {'form': form})  # Pass the form to the template
        
def user_login(request):
    # return HttpResponse(request.user)
    if request.method == "GET":
        # form = UserCreationForm()
        
        form = UserCreateForm()
        
        # return HttpResponse(form)
        return render(request,'login.html',{'form':form} )
    else:
        # return HttpResponse( request.POST )  
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request,  email=email, password= password)

        if user is None:
            return HttpResponse('invalid credentials!!!')
        else:
            login(request,user)
            return HttpResponse('successfully logged in!!')
            return HttpResponse(request)
def user_logout(request):
    logout(request)
    return HttpResponse('User is Successfully logged out!!!')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse ('Your message has been sent successfully!')
            
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


# def add_to_cart(request, product_id):
#     cart = request.session.get('cart', {})
#     cart[str(product_id)] = cart.get(str(product_id), 0) + 1
#     request.session['cart'] = cart

#     print("Cart now contains:", request.session['cart'])  # ✅ Safe to use here

#     return redirect('cart')
