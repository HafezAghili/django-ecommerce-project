from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('comingsoon/',ComingSoonView.as_view(),name='comingsoon'),
    path('panel/',PanelView.as_view(),name='panel'),

    #product
    path('product/',ProductListView.as_view(),name='product_view'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'), 
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]