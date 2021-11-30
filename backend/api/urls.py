from api import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register('contact-requests', views.ContactFormViewSet)
router.register('portfolios', views.PortfolioViewSet)

urlpatterns = [
    path('', include(router.urls))
]
