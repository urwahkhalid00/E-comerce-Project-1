from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('products/',views.product_list, name='product_list'),
    # path('product/detail/',views.product_detail, name='product_detail'),
    path('products/detail/<id>/',views.product_detail, name='product_detail'),
    path('brands/', views.brand_list, name='brand_list'),
    path('cart',views.cart, name='cart'),
    path('cart/add', views.add_to_cart ,name='add_to_cart'),
    path('cart/delete/<int:cart_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('checkout',views.checkout, name='checkout'),
    path('my-account',views.my_account, name='my-account'),
    path('wishlist',views.wishlist, name='wishlist'),
    path('login/', views.user_login,name='login'),
    path('register/', views.register ,name='register'),
    path('logout/', views.user_logout ,name='logout'),
    path('contact/', views.contact, name='contact'),  
    # path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]