from rest_framework import serializers
from basic_info.models import ContactFormModel, PortfolioModel


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormModel
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioModel
        fields = '__all__'
