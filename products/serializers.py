from django import forms
from .models import Products
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    # my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Products
        fields = '__all__'

        # fields = ('title', 'content', 'price', 'sale_price')
















