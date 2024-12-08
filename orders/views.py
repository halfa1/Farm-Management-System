
# Create your views here.
from products.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Order
from admin_panel.models import Worker

@login_required
def products_view(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        # if quantity > product.availability:
        #     messages.error(request, "Quantity exceeds availability.")
        #     return redirect('products')
        Order.objects.create(user=request.user, product=product, quantity=quantity)
        # order = Order.objects.create(
        #         user=request.user,
        #         product=product,
        #         quantity=quantity,
        #         total_price=quantity * product.price_per_quantity
        #     )
        #product.availability -= quantity
        product.save()
        messages.success(request, "Order placed successfully.")
        return redirect('cart')
    return render(request, 'orders/order_form.html', {'product': product})


@login_required
def admin_panel(request):
    if not request.user.is_staff:
        return redirect('home')
    workers = Worker.objects.all()
    return render(request, 'products/admin_panel.html', {'workers': workers})



@login_required
def view_cart(request):
    orders = Order.objects.filter(user=request.user)
    total_price = sum(order.total_price() for order in orders)
    return render(request, 'orders/cart.html', {'orders': orders, 'total_price': total_price})


@login_required
def remove_from_cart(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    order.delete()
    messages.success(request, "Item removed from your cart.")
    return redirect('cart')
