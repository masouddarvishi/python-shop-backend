from django.urls import path
from .views import productView

urlpatterns = [
    path('store', productView.ProductController.store, name='product.store')
]