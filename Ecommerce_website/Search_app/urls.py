from django.urls import path

from . import views

app_name = 'Search_app'
urlpatterns = [
    path('', views.search_all, name='search_all')
]
