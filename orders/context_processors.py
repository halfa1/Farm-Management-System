from orders.models import Order

def cart_count(request):
    if request.user.is_authenticated:
        count = Order.objects.filter(user=request.user).count()
        return {'cart_count': count}
    return {'cart_count': 0}