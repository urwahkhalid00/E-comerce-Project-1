from django.contrib import admin
from .models import Category, Product, Brand, Cart,Contact, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'rating', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product','qty','sub_total' , 'user')
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name','email','country', 'order_price')
        
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Contact, ContactAdmin) 
admin.site.register(Order,OrderAdmin )  


