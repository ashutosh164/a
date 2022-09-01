from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from products.models import Products
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
from rest_framework import generics


@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    if request.method == "GET":
        product = Products.objects.all()
        seria = ProductSerializer(product, many=True)
        return Response(seria.data)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # print(serializer.data)
            # data = serializer.data
            return Response(serializer.data)






