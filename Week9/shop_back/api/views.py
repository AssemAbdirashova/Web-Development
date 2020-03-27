import json

from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Category
from django.http import Http404
# Create your views here.


# products = []
# for i in range(1, 5):
#     products.append(
#         {
#             'id': i,
#             'name': f'product {i}',
#             'price': i * 1000
#         }
#     )

# products = [
#     {
#     'id': i,
#     'name': f'product {i}',
#     'price': i * 1000
#     } for i in range(1,5)
# ]

def product_list(request):
    #SELECT * FROM api_product
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe = False)

def product_detail(request, product_id):
    #SELECT * FROM api_product WHERE id = <product_id>
    try:
        product = Product.objects.get(id = product_id)
    except Product.DoesNotExist as e:
        raise Http404
    return JsonResponse(product.to_json())

def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

def one_category(request, category_id):
    try:
        category = Category.objects.get(id = category_id)
    except Category.DoesNotExist as e:
        raise Http404
    return JsonResponse(category.to_json())

def category_products(request, id):
    products = Product.objects.all()
    main_info = []
    for item in products:
        if item.category_id.id == id:
            main_info.append(item.to_json())
    return JsonResponse(main_info, safe = False)

#def category_list():