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

class CategoryUpdateView(UpdateView): 
    model = Category
    template_name = 'panel/category/category_update.html'
    fields =  '__all__'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'panel/category/category_delete.html'
    success_url = reverse_lazy('product_view')


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
