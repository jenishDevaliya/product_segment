from django.urls import path
from .views import ProductSegmentAPIView

urlpatterns = [
    path('products/', ProductSegmentAPIView.as_view(), name='product-segment'),
]
