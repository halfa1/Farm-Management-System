
from django.shortcuts import render
from .models import Product, Category

def products_view(request):
    category_id = request.GET.get('category')  # Get the category ID from the query parameter
    categories = Category.objects.all()       # Fetch all categories
    if category_id:
        products = Product.objects.filter(category_id=category_id)  # Filter products by category
    else:
        products = Product.objects.all()  # Fetch all products if no category is selected

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'products/productlist.html', context)
