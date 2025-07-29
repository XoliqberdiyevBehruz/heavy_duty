from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import BaseModel


class UsageArea(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_('nom'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Soha")
        verbose_name_plural = _('Sohalar')


class ProductCategory(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_('kategoriya nomi'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Mahsulot kategoriyasi')
        verbose_name_plural = _('Mahsulot kategoriyalari')


class Product(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_("mahsulot nomi"))
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name='products',
        verbose_name=_("mahsulot kategoriyasi")
    )
    model = models.CharField(max_length=200, verbose_name=_("mahsulot modeli"))
    description = models.TextField(verbose_name=_('mahsulot haqida'))
    usage_area = models.ManyToManyField(
        UsageArea, related_name='products', verbose_name=_("qo'llash sohalari")
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Mahsulot')
        verbose_name_plural = _('Mahsulotlar')


class ProductFeature(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('xususiyat'))
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_features',
        verbose_name=_('mahsulot')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Mahsulot xususiyati')
        verbose_name_plural = _('Mahsulot xususiyatlari')


class ProductMedia(BaseModel):
    media = models.ImageField(upload_to='product/product_media/', verbose_name=_('rasm'))
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_medias',
        verbose_name=_('maxsulot')
    )
    
    def __str__(self):
        return f'{self.product} media {self.media.name}'
    
    class Meta:
        verbose_name = _('Mahsulot rasmi')
        verbose_name_plural = _('Mahsulot rasmlari')
    

class ProductTechnicalSpecifications(models.Model):
    TYPE = (
        ('CHEMICAL_COMPOSITION', 'Kimyoviy Tarkib'),
        ('MECHANICAL_PROPERTIES', 'Mexanik Xususiyatlar'),
        ('PHYSICAL_PROPERTIES', 'Fizik Xususiyatlar'),
        ('PACKAGING_AND_STORAGE', 'Qadoqlash va Saqlash')
    )
    name = models.CharField(max_length=200, verbose_name=_('nomi'))
    amount = models.CharField(max_length=200, verbose_name=_('miqdori'))
    type = models.CharField(max_length=21, verbose_name=_('turi'), choices=TYPE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tech_specifications')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Mahsulot texnik xususiyati')
        verbose_name_plural = _('Mahsulot texnik xususiyati')