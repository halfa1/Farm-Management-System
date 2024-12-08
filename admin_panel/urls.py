from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('orders/', views.view_orders, name='view_orders'),
    path('search-orders/', views.search_orders, name='search_orders'),
]
