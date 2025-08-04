from rest_framework import serializers

from apps.common import models


class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = [
            'id', 'title', 'description', 'banner', 'page'
        ]


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Settings
        fields = [
            'id', 'location_text', 'first_email', 'second_email', 'first_phone', 'second_phone',
            'facebook_url', 'instagram_url', 'telegram_url', 'youtube_url', 'text'
        ]


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutUs
        fields = [
            'id', 'text', 'image'
        ]

class StatistcSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Statistics
        fields = [
            'id', 'name', 'count'
        ]


class SertificateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sertificate
        fields = [
            'id', 'sertificate'
        ]


class ProductInfoListSerialzier(serializers.ModelSerializer):
    class Meta:
        model = models.ProductInfo
        fields = [
            'id', 'name', 'hs_code'
        ]


class CompanyContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyContactInfo
        fields = [
            'phone_number_1', 'phone_number_2', 'phone_number_3', 
            'email_1', 'email_2', 'email_3', 'address', 
            'working_hours_monday_fridy', 'working_hours_saturday', 'working_hours_sunday'
        ]


class ContactUsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = [
            'full_name', 'phone_number', 'email', 
            'message'
        ]