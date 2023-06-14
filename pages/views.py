from django.views.generic import TemplateView , CreateView , ListView , UpdateView  , DetailView , DeleteView
from .models import *
from django.urls import reverse_lazy #for delete
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ComingSoonView(TemplateView):
    template_name = 'ComingSoon.html'

class PanelView(TemplateView):
    template_name = 'panel/panel.html'


#USER VIEWS-------------------
# Product views
class ProductListView(ListView):
    model = Product
    template_name = 'product_view.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['supplier_list'] = self.object.supplier.all()
        return context


#ADMIN VIEWS-------------------
# Category views
class CategoryListView(ListView):
    model = Category
    template_name = 'panel/category/category_view.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'panel/category/category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'panel/category/category_create.html'
    fields = '__all__'
    success_url = reverse_lazy('category_view')

class CategoryUpdateView(UpdateView): 
    model = Category
    template_name = 'panel/category/category_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('category_view')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'panel/category/category_delete.html'
    success_url = reverse_lazy('category_view')


# Supplier views
class SupplierListView(ListView):
    model = Supplier
    template_name = 'panel/supplier/supplier_view.html'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'panel/supplier/supplier_detail.html'

class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'panel/supplier/supplier_create.html'
    fields = '__all__'
    success_url = reverse_lazy('supplier_view')

class SupplierUpdateView(UpdateView): 
    model = Supplier
    template_name = 'panel/supplier/supplier_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('supplier_view')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'panel/supplier/supplier_delete.html'
    success_url = reverse_lazy('supplier_view')


# City views
class CityListView(ListView):
    model = City
    template_name = 'panel/city/city_view.html'

class CityDetailView(DetailView):
    model = City
    template_name = 'panel/city/city_detail.html'

class CityCreateView(CreateView):
    model = City
    template_name = 'panel/city/city_create.html'
    fields = '__all__'
    success_url = reverse_lazy('city_view')

class CityUpdateView(UpdateView): 
    model = City
    template_name = 'panel/city/city_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('city_view')

class CityDeleteView(DeleteView):
    model = City
    template_name = 'panel/city/city_delete.html'
    success_url = reverse_lazy('city_view')    


# Product views
class ProductListViewAdmin(ListView):
    model = Product
    template_name = 'panel/product/product_view_admin.html'

class ProductDetailViewAdmin(DetailView):
    model = Product
    template_name = 'panel/product/product_detail_admin.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailViewAdmin, self).get_context_data(**kwargs)
        context['supplier_list'] = self.object.supplier.all()
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = 'panel/product/product_create.html'
    fields = '__all__'
    success_url = reverse_lazy('product_view_admin')

class ProductUpdateView(UpdateView): 
    model = Product
    template_name = 'panel/product/product_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('product_view_admin')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'panel/product/product_delete.html'
    success_url = reverse_lazy('product_view_admin')
