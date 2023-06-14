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

    ##supplier
    path('panel/supplier/',SupplierListView.as_view(),name='supplier_view'),
    path('panel/supplier/new/', SupplierCreateView.as_view(), name='supplier_create'),
    path('panel/supplier/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('panel/supplier/<int:pk>/edit/', SupplierUpdateView.as_view(), name='supplier_update'), 
    path('panel/supplier/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),

    ##city
    path('panel/city/',CityListView.as_view(),name='city_view'),
    path('panel/city/new/', CityCreateView.as_view(), name='city_create'),
    path('panel/city/<int:pk>/', CityDetailView.as_view(), name='city_detail'),
    path('panel/city/<int:pk>/edit/', CityUpdateView.as_view(), name='city_update'), 
    path('panel/city/<int:pk>/delete/', CityDeleteView.as_view(), name='city_delete'),

    #product
    path('product/',ProductListView.as_view(),name='product_view'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]