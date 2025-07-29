from rest_framework import generics, status
from rest_framework.response import Response

from apps.common import serializers, models


class BannerListApiView(generics.ListAPIView):
    serializer_class = serializers.BannerListSerializer
    queryset = models.Banner.objects.order_by('-created_at')


class SettingsApiView(generics.GenericAPIView):
    serializer_class = serializers.SettingsSerializer
    queryset = models.Settings.objects.all()
    
    def get(self, request):
        settings = models.Settings.objects.first()
        serializer = self.serializer_class(settings)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AboutUsApiView(generics.GenericAPIView):
    serializer_class = serializers.AboutUsSerializer
    queryset = models.AboutUs.objects.all()
    
    def get(self, request):
        settings = models.AboutUs.objects.first()
        serializer = self.serializer_class(settings)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class StatiscsApiView(generics.ListAPIView):
    serializer_class = serializers.StatistcSerializer
    queryset = models.Statistics.objects.all()
    

class SertificateListApiView(generics.ListAPIView):
    serializer_class = serializers.SertificateListSerializer
    queryset = models.Sertificate.objects.all()


class ProductInfoListApiView(generics.ListAPIView):
    serializer_class = serializers.ProductInfoListSerialzier
    queryset = models.ProductInfo.objects.all()


class CompanyContactInfoApiView(generics.GenericAPIView):
    serializer_class = serializers.CompanyContactInfoSerializer
    queryset = models.CompanyContactInfo.objects.all()

    def get(self, request):
        settings = models.CompanyContactInfo.objects.first()
        serializer = self.serializer_class(settings)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactUsApiView(generics.CreateAPIView):
    serializer_class = serializers.ContactUsCreateSerializer
    queryset = models.ContactUs.objects.all()