from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='list_products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='detail_products'),
    path('admin_product_list/', AdminProductListView.as_view(), name='admin_product_list'),
    path('admin_add_product', AdminAddProductView.as_view(), name='admin_add_product'),
    path('admin_edit_product/<int:pk>/', AdminEditProductView.as_view(), name='admin_edit_product'),
    path('admin_delete_product/<int:pk>/', AdminDeleteProductView.as_view(), name='admin_delete_product'),
]
