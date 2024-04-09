from rest_framework import serializers

from apps.products.models import *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"