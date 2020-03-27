from django.urls import path

from api.views import product_list, product_detail, category_list, one_category, category_products

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/', category_list),
    path('categories/<int:id>/', one_category),
    path('categories/<int:id>/products/', category_products)
]