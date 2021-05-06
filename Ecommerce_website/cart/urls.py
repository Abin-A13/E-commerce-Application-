from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_details, name='cart_details'),
    path('minus/<int:product_id>/',views.cart_minus, name='minus'),
    path('delete/<int:product_id>/',views.all_delete, name='delete')
]
