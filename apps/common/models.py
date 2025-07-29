from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import BaseModel


class Banner(BaseModel):
    PAGE = (
        ('HOME', _('bosh sahifa')),
        ('ABOUT', _('biz haqimizda')),
        ('PRODUCTS', _('maxsulotlar')),
        ('CONTACT', _("biz bilan bo'glanish")),
    )

    title = models.CharField(max_length=100, verbose_name=_('sarlovha'))
    description = models.TextField(verbose_name=_('tavsif'))
    banner = models.ImageField(upload_to='common/banner/')
    page = models.CharField(max_length=50, choices=PAGE)

    def __str__(self):
        return f"{self.title} - {self.page}"
    
    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('bannerlar')


class Settings(BaseModel):
    location_text = models.CharField(verbose_name=_('lokatsiya'), max_length=200)
    email = models.EmailField(verbose_name=_("elektron po'chta"))
    
    first_phone = models.CharField(
        max_length=13, null=True, blank=True, verbose_name=_('birinchi raqam')
    )
    second_phone = models.CharField(
        max_length=13, null=True, blank=True, verbose_name=_('ikkinchi raqam')
    )

    facebook_url = models.URLField(verbose_name=_('facebook link'))
    instagram_url = models.URLField(verbose_name=_('instagram link'))
    telegram_url = models.URLField(verbose_name=_('telegram link'))
    youtube_url = models.URLField(verbose_name=_('youtube link'))

    text = models.TextField(verbose_name=_('text'))

    class Meta:
        verbose_name = _('Sozlama')
        verbose_name_plural = _('Sozlamalar')


class AboutUs(BaseModel):
    text = models.TextField(verbose_name=_('text'))
    image = models.ImageField(upload_to='common/about_us/')

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimizda"


class Statistics(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_('statistika nomi'))
    count = models.CharField(max_length=20, verbose_name=_('statistika'))

    class Meta:
        verbose_name = _('kompaniy statistikasi')
        verbose_name_plural = _('kompaniy statistikasi')


class Sertificate(BaseModel):
    sertificate = models.ImageField(upload_to='common/sertificate/', verbose_name=_('sertifikat'))

    class Meta:
        verbose_name = _('sertifikat')
        verbose_name_plural = _('sertifikatlar')


class ProductInfo(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_('maxsulot nomi'))
    hs_code = models.CharField(max_length=200, verbose_name=_('hs kodi'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("maxsulot haqida")
        verbose_name_plural = _("maxsulotlar haqida")


class CompanyContactInfo(BaseModel):
    phone_number_1 = models.CharField(
        max_length=15, null=True, blank=True,
        verbose_name=_('birinchi telefon raqam'),
    )
    phone_number_2 = models.CharField(
        max_length=15, null=True, blank=True,
        verbose_name=_('ikkinchi telefon raqam')
    )
    phone_number_3 = models.CharField(
        max_length=15, null=True, blank=True,
        verbose_name=_('uchunchi telefon raqam')
    )

    email_1 = models.EmailField(
        null=True, blank=True, 
        verbose_name=_('birinchi email')
    )
    email_2 = models.EmailField(
        null=True, blank=True, 
        verbose_name=_('ikkinchi email')
    )
    email_3 = models.EmailField(
        null=True, blank=True,
        verbose_name=_('uchinchi email')    
    )

    working_hours_monday_fridy = models.CharField(max_length=100, verbose_name=_(
        'dushanbadan jumagacha ish soatlari'
    )) 
    working_hours_saturday = models.CharField(max_length=200, verbose_name=_(
        'shanba kuni ish soatlari'
    ))
    working_hours_sunday = models.CharField(
        max_length=200, verbose_name=_('yakshanba kuni ish soatlari'),
        null=True, blank=True, default='Yopiq'
    )

    address = models.CharField(
        max_length=200, verbose_name=_('lokatsiya')
    )

    class Meta:
        verbose_name = _("kompaniyaning aloqa ma'lumoti")
        verbose_name_plural = _("kompaniyaning aloqa ma'lumotlari")
    

class ContactUs(BaseModel):
    SUBJECT = (
        ('PRODUCT_INQUIRY', "mahsulot so'rovi"),
        ('TECHNICAL_SUPPORT', 'texnik yordam'),
        ('PARTNERSHIP', 'hamkorlik'),
        ('COMPLAINT', 'shikoyat'),
        ('OTHER', 'boshqa'),
    )
    is_contacted = models.BooleanField(default=False, verbose_name=_("aloqaga chiqilganmi"))
    full_name = models.CharField(max_length=100, verbose_name=_("to'liq ism sharif"))
    email = models.EmailField(verbose_name=_('elektron pochta'))
    phone_number = models.CharField(max_length=15, verbose_name=_("telefon raqam"))
    company_name = models.CharField(max_length=200, verbose_name=_("companiya nomi"))
    message = models.TextField(verbose_name=_('xabar'))
    subject = models.CharField(max_length=200, choices=SUBJECT)

    class Meta:
        verbose_name = _('aloqa uchun xabar')
        verbose_name_plural = _('aloqa uchun xabarlar')

