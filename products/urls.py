from django.contrib import admin
from django.urls import path
from .views import ProductDetailAPIView, ProcudtCreateView, \
    ProductList, ProductListCreateView, ProductUpdateView, DeleteView

urlpatterns = [
    path('list/', ProductList.as_view()),
    path('product/', ProductListCreateView.as_view()),
    path('create/', ProcudtCreateView.as_view()),
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('<int:pk>/update/', ProductUpdateView.as_view()),
    path('<int:pk>/delete/', DeleteView.as_view()),

]




