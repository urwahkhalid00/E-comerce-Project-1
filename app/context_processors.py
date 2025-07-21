from .models import Cart

def cart_item_count(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.id)
        total_quantity = sum(item.qty for item in cart_items)
    else:
        total_quantity = 0

    return {'cart_item_count': total_quantity}
