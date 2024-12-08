from django.urls import path
from products.views import products_view
from admin_panel.views import admin_dashboard
from orders.views import view_cart,add_to_cart
from . import views

urlpatterns = [
    path('',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('products/',products_view,name='products'),
    path('admin_panel/',admin_dashboard ,name='admin_panel'),
    path('order/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('orders/', view_cart,name='cart')
]