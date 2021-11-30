from django.shortcuts import render
from rest_framework import viewsets, status
from api.models import ContactForm, Portfolio
from api import serializers
from rest_framework.response import Response


class ContactFormViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContactFormSerializer
    queryset = ContactForm.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Done! we will contact you soon'}, status=status.HTTP_201_CREATED)
        return Response({"message": "Something is wrong. Please provide accurate information."}, status=status.HTTP_400_BAD_REQUEST)


class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PortfolioSerializer
    queryset = Portfolio.objects.all()
