from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response

from apps.products import serializers, models

class ProductCategoryListApiView(generics.ListAPIView):
    serializer_class = serializers.ProductCategoryListSerializer
    queryset = models.ProductCategory.objects.all()


class ProductListApiView(generics.GenericAPIView):
    serializer_class = serializers.ProductListSerializer
    queryset = models.Product.objects.all()
    
    def get(self, request, category_id):
        category = get_object_or_404(models.ProductCategory, id=category_id)
        
        products = models.Product.objects.filter(category=category)\
        .prefetch_related(
            'product_features', 'product_medias', 'product_tech_specifications', 'usage_area'
        )
        
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailApiView(generics.RetrieveAPIView):
    serializer_class = serializers.ProductListSerializer
    queryset = models.Product.objects.all()
    lookup_field = 'id'


class ProductApiView(generics.RetrieveAPIView):
    serializer_class = serializers.ProductListSerializer
    queryset = models.Product.objects.all()

