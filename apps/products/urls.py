from apps.products.views import *
from django.urls import path



urlpatterns = [
    path('', ProductAPIView.as_view(), name = "api_products")
]