
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import FarmBlock, Worker
from orders.models import Order

# Only admins can access these views
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_dashboard(request):
    blocks = FarmBlock.objects.all()
    workers = Worker.objects.all()
    orders = Order.objects.all()
    return render(request, 'admin_panel/dashboard.html', {
        'blocks': blocks,
        'workers': workers,
        'orders': orders,
    })


@user_passes_test(is_admin)
def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'admin_panel/orders.html', {'orders': orders})


@user_passes_test(is_admin)
def search_orders(request):
    query = request.GET.get('query')
    results = Order.objects.filter(user__username__icontains=query)
    return render(request, 'admin_panel/search_results.html', {'results': results, 'query': query})
