from modeltranslation.translator import register, TranslationOptions

from apps.products import models


@register(models.UsageArea)
class UsageAreaTranslation(TranslationOptions):
    fields = ['name']


@register(models.ProductCategory)
class ProductCategoryTranslation(TranslationOptions):
    fields = ['name']


@register(models.Product)
class ProductTranslation(TranslationOptions):
    fields = [
        'name', 'description'
    ]


@register(models.ProductFeature)
class ProductFeatureTranslation(TranslationOptions):
    fields = ['name']


@register(models.ProductTechnicalSpecifications)
class ProductTechnicalSpecificationTranslation(TranslationOptions):
    fields = ['name']
