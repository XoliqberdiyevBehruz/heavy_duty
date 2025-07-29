from rest_framework import serializers

from apps.products import models


class ProductCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = [
            'id', 'name',
        ]


class UsageAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsageArea
        fields = ['id', 'name']


class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductFeature
        fields = [
            'id', 'name'
        ]


class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductMedia
        fields = ['id', 'media']


class ProductTechnicalSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductTechnicalSpecifications
        fields = [
            'id', 'name', 'amount', 'type'
        ] 


class ProductListSerializer(serializers.ModelSerializer):
    usage_area = UsageAreaSerializer(many=True, read_only=True)
    product_features = ProductFeatureSerializer(many=True, read_only=True)
    product_medias = ProductMediaSerializer(many=True, read_only=True)
    product_tech_specifications = ProductTechnicalSpecificationSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = [
            'id', 'name', 'model', 'description', 'usage_area', 
            'product_features', 'product_medias', 'product_tech_specifications', 
        ]