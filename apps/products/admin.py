from django.contrib import admin

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from apps.products import models

#######################
# Admin Inlines
######################
class ProductMediaInline(admin.TabularInline):
    model = models.ProductMedia
    extra = 0


class ProductFeatureInline(TranslationTabularInline):
    model = models.ProductFeature
    extra = 0


class ProductTechnicalSpecificationsInline(TranslationTabularInline):
    model = models.ProductTechnicalSpecifications
    extra = 0


########################
# Admin Panels
########################
@admin.register(models.UsageArea)
class UsageAreaAdmin(TranslationAdmin):
    list_display = ['name']


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    list_display = ['name']


@admin.register(models.Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['name', 'model', 'category']
    inlines = [ProductMediaInline, ProductFeatureInline, ProductTechnicalSpecificationsInline]


@admin.register(models.ProductFeature)
class ProductFeatureAdmin(TranslationAdmin):
    list_display = ['name', 'product']


@admin.register(models.ProductMedia)
class ProductMediaAdmin(admin.ModelAdmin):
    list_display = ['media', 'product']


@admin.register(models.ProductTechnicalSpecifications)
class ProductTechnicalSpecificationAdmin(TranslationAdmin):
    list_display = ['name', 'amount', 'type']