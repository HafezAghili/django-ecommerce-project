from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('comingsoon/',ComingSoonView.as_view(),name='comingsoon'),
    path('panel/',PanelView.as_view(),name='panel'),
    
    #panel
    ##product
    path('panel/product/',ProductListViewAdmin.as_view(),name='product_view_admin'),
    path('panel/product/new/', ProductCreateView.as_view(), name='product_create'),
    path('panel/product/<int:pk>/', ProductDetailViewAdmin.as_view(), name='product_detail_admin'),
    path('panel/product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'), 
    path('panel/product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    ##category
    path('panel/category/',CategoryListView.as_view(),name='category_view'),
    path('panel/category/new/', CategoryCreateView.as_view(), name='category_create'),
    path('panel/category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('panel/category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'), 
    path('panel/category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    #product
    path('product/',ProductListView.as_view(),name='product_view'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]