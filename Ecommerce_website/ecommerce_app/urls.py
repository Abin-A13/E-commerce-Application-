
from django.urls import path

from . import views

app_name = 'ecommerce_app'
urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_cat'),
    path('<slug:c_slug>/<slug:prod_slug>/', views.product_details, name='prodCat'),

]
