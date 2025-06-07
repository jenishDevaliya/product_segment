from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductSegmentAPIView(APIView):
    def get(self, request):
        
        price_min = request.GET.get('price_min', None)
        price_max = request.GET.get('price_max', None)
        size_min = request.GET.get('size_min', None)
        size_max = request.GET.get('size_max', None)

        products = Product.objects.all()

    
        if price_min is not None:
            products = products.filter(price__gte=price_min)
        if price_max is not None:
            products = products.filter(price__lte=price_max)

        
        if size_min is not None:
            products = products.filter(size__gte=size_min)
        if size_max is not None:
            products = products.filter(size__lte=size_max)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
