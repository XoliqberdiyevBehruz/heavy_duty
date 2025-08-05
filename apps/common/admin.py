from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from apps.common import models


@admin.register(models.Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ['title', 'description']


@admin.register(models.Settings)
class SettingsAdmin(TranslationAdmin):
    list_display = ['location_text', 'first_email']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True
    

@admin.register(models.AboutUs)
class AboutUsAdmin(TranslationAdmin):
    list_display = ['image', 'text']
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True
    

@admin.register(models.Statistics)
class StatictsAdmin(TranslationAdmin):
    list_display = ['name', 'count']


@admin.register(models.Sertificate)
class SertificateAdmin(admin.ModelAdmin):
    list_display = ['sertificate', 'created_at']


@admin.register(models.ProductInfo)
class ProductInfoAdmin(TranslationAdmin):
    list_display = ['name', 'hs_code']

@admin.register(models.CompanyContactInfo)
class ConpanyContactInfoAdmin(TranslationAdmin):
    list_display = [
        'phone_number_1', 'phone_number_2', 'address',
    ]

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return True
    
@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        'full_name', 'phone_number', 'is_contacted'
    ]  
    list_filter = [
        'is_contacted',
    ]

    def has_add_permission(self, request):
        return False