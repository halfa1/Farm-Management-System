from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('remove-from-cart/<int:order_id>/', views.remove_from_cart, name='remove_from_cart'),
    #path('place-order/<int:product_id>/', views.place_order, name='place_order'),
]
