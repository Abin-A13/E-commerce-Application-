from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from ecommerce_app.models import Product


def search_all(request):
    query = None
    products = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(descriptions__contains=query))
    return render(request, "search.html", {'query': query, 'products': products})
