from modeltranslation.translator import register, TranslationOptions

from apps.common import models


@register(models.Banner)
class BannerTranslation(TranslationOptions):
    fields = ['title', 'description']


@register(models.Settings)
class SettingsTranslation(TranslationOptions):
    fields = ['text']


@register(models.AboutUs)
class AboutUsTranslation(TranslationOptions):
    fields = ['text']


@register(models.ProductInfo)
class ProductInfoTranslation(TranslationOptions):
    fields = ['name']
    
@register(models.Statistics)
class StatisticsTranslation(TranslationOptions):
    fields = ['name']

@register(models.CompanyContactInfo)
class CompanyContactInfoTranslation(TranslationOptions):
    fields = ['address']