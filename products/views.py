from products.serializers import ProductSerializer
from rest_framework import generics, mixins, permissions, authentication
from .models import Products
from .permission import IsStaffPermission
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.aithentication import TokenAuth


class ProcudtCreateView(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


class ProductList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.TokenAuthentication]


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication,TokenAuth]
    # permission_classes = [permissions.DjangoModelPermissions]
    permission_classes = [IsStaffPermission]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class DeleteView(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# def get_alt_view(request, *args, **kwargs):
#     method = request.method
#
#     if method == 'GET':
#         pass
#         queryset = Products.objects.all()
#         data = ProductSerializer(queryset, many=True).data
#         return
#     if method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             print(serializer.data)
#             return Response(serializer.data)
#         return Response({'invalid': 'not good data'}, status=400)





