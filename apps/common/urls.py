from django.urls import path 

from apps.common import views

urlpatterns = [
    path('banners/', views.BannerListApiView.as_view(), name='banner list'),
    path('settings/', views.SettingsApiView.as_view(), name='settings'),
    path('about_us/', views.AboutUsApiView.as_view(), name='about us'),
    path('statistcs/', views.StatiscsApiView.as_view(), name='statistics'),
    path('sertificate/', views.SertificateListApiView.as_view(), name='sertificate'),
    path('product_infos/', views.ProductInfoListApiView.as_view(), name='product infos'),
    path('company_contact_info/', views.CompanyContactInfoApiView.as_view()),
    path('contact_us/', views.ContactUsApiView.as_view()),
]